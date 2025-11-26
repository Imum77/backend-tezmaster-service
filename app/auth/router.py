from fastapi                import APIRouter, Depends, Query, Form
from typing                 import List
from sqlalchemy.ext.asyncio import AsyncSession
import aiohttp

from auth.schemas           import Verify, VerifyResponse,  AuthHistoryResponse, LogoutResponse

from db                     import get_db
from auth.crud              import get_auth_history_db, auth_verify, auth_otp, deactivate_user
from auth.utils.utils       import verify_access_token
from dependencies.session   import get_http_session

router = APIRouter()


@router.post("/auth/otp")
async def get_auth_otp(phone: str = Form(...),  db: AsyncSession = Depends(get_db), session: aiohttp.ClientSession = Depends(get_http_session)):
    return await auth_otp(
        msisdn=phone,
        db=db,
        session=session
    )


@router.post("/auth/verify", response_model=VerifyResponse)
async def get_auth_verify(request: Verify = Form(...), db: AsyncSession = Depends(get_db)):
    return await auth_verify(
        db=db,
        phone=request.phone,
        otp=request.otp,
        stt=request.stt
    )


@router.get("/auth/history", response_model=List[AuthHistoryResponse])
async def get_auth_history(
        msisdn: str = Query(min_length=12, max_length=12),
        db: AsyncSession = Depends(get_db)
    ):

    return await get_auth_history_db(db=db, msisdn=msisdn)



@router.get("/auth/logout", response_model=LogoutResponse)
async def logout(msisdn: str = Depends(verify_access_token), db: AsyncSession = Depends(get_db)):

    return await deactivate_user(db=db, msisdn=msisdn)