from fastapi            import APIRouter, Depends, Query, Body, Request
from typing             import List
from sqlalchemy.orm     import Session
from db                 import get_db
from auth.schemas       import Verify, VerifyResponse,  AuthHistoryResponse, LogoutResponse, OtpSchema
from auth.crud          import get_auth_history_db, auth_verify, auth_otp, deactivate_user
from auth.utils.utils   import verify_access_token


router = APIRouter()


@router.post("/auth/otp")
async def get_auth_otp(request: Request,  db: Session = Depends(get_db)):
    raw_body = await request.body()
    print("RAW BODY:", raw_body, raw_body.decode())
    return auth_otp(
        msisdn='992777003304',
        db=db
    )


@router.post("/auth/verify", response_model=VerifyResponse)
def get_auth_verify(request: Verify, db: Session = Depends(get_db)):
    return auth_verify(
        db=db,
        phone=request.phone,
        otp=request.otp,
        stt=request.stt
    )


@router.get("/auth/history", response_model=List[AuthHistoryResponse])
def get_auth_history(
        msisdn: str = Query(min_length=12, max_length=12),
        db: Session = Depends(get_db)
    ):

    return get_auth_history_db(db=db, msisdn=msisdn)



@router.get("/auth/logout", response_model=LogoutResponse)
def logout(msisdn: str = Depends(verify_access_token), db: Session = Depends(get_db)):

    return deactivate_user(db=db, msisdn=msisdn)