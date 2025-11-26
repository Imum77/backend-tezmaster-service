from fastapi                import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future      import select
from auth.models            import AuthHistory
from datetime               import datetime, timedelta
from auth.schemas           import TokenSchema, VerifyResponse, SttToken, AuthOtpResponse, LogoutResponse
from auth.utils.utils       import generate_access, generate_refresh, decode, generate_otp, generate_stt



async def auth_otp(msisdn: str, db: AsyncSession, session):
    otp = await generate_otp(msisdn, session)
    stt = SttToken(stt=generate_stt(otp))
    
    new_record = AuthHistory(
        phone        =  msisdn,
        otp          =  otp,
        verified     =  False,
        create_date  =  datetime.utcnow(),
        updated_date =  datetime.utcnow(),
        device_os    =  None,
        token        =  stt,
        active       =  False,
        device_model =  None,
        device_ip    =  None,
    )
    db.add(new_record)
    await db.commit()
    await db.refresh(new_record)
    return  AuthOtpResponse(
        data=stt
    )


async def auth_verify(db: AsyncSession, phone: str, otp: str, stt: str ):

    result = await db.execute(
        select(AuthHistory)
        .where(AuthHistory.phone == phone)
        .where(AuthHistory.otp == otp)
    )
    record = result.scalar_one_or_none()

    if not record:
        raise HTTPException(status_code=404, detail="OTP not found")

    if record.create_date + timedelta(minutes=25) < datetime.utcnow():
        raise HTTPException(status_code=400, detail="OTP expired")

    if not decode(stt):
        raise HTTPException(status_code=400, detail="Invalid STT")

    if record.verified:
        raise HTTPException(status_code=400, detail="OTP already used")

    record.verified = True
    record.updated_date = datetime.utcnow()
    record.active = True


    access_token = generate_access({"sub": record.phone})
    refresh_token = generate_refresh({"sub": record.phone})

    await db.commit()
    await db.refresh(record)

    tokens =  TokenSchema(
        access_token=access_token,
        refresh_token=refresh_token
    )

    return VerifyResponse(
        data=tokens
    )


async def get_auth_history_db(db: AsyncSession, msisdn: str):
    result = await db.execute(select(AuthHistory).where(AuthHistory.phone == msisdn))
    return result.scalars().all()



async def deactivate_user(msisdn: str, db: AsyncSession):
    result = await db.execute(select(AuthHistory).where(AuthHistory.phone == msisdn).where(AuthHistory.active == True))
    auth_history = result.scalars().first()

    if auth_history:
        auth_history.active = False
        await db.commit()
        await db.refresh(auth_history)

    return LogoutResponse