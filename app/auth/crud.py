from fastapi            import HTTPException
from sqlalchemy.orm     import Session
from auth.models        import AuthHistory
from datetime           import datetime, timedelta
from auth.schemas       import TokenSchema, VerifyResponse, SttToken, AuthOtpResponse, LogoutResponse
from auth.utils.utils   import generate_access, generate_refresh, decode, generate_otp, generate_stt



def auth_otp(msisdn: str, db: Session):
    otp = generate_otp(msisdn)
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
    db.commit()
    db.refresh(new_record)

    return  AuthOtpResponse(
        data=stt
    )



def auth_verify(db: Session, phone: str, otp: str, stt: str ):

    record = (
        db.query(AuthHistory)
        .filter(AuthHistory.phone == phone)
        .filter(AuthHistory.otp == otp)
        .first()
    )

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

    db.commit()
    db.refresh(record)

    tokens =  TokenSchema(
        access_token=access_token,
        refresh_token=refresh_token
    )

    return VerifyResponse(
        data=tokens
    )


def get_auth_history_db(db: Session, msisdn: str):
    return db.query(AuthHistory).filter(AuthHistory.phone == msisdn).all()


def deactivate_user(msisdn: str, db: Session):
    auth_history = (
        db.query(AuthHistory)
        .filter(AuthHistory.phone == msisdn, AuthHistory.active == True)
        .first()
    )

    if auth_history:
        auth_history.active = False
        db.commit()

    return LogoutResponse