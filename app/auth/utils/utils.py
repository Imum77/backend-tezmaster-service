from fastapi    import Header, HTTPException, status
from fastapi.responses import JSONResponse
from jose       import JWTError
import jwt
import conf as conf
from datetime   import datetime, timedelta, timezone


def generate_refresh(phone: str):
    dt = datetime.now(timezone.utc) + timedelta(days=30)
    token = jwt.encode({
            'number': phone,
            'exp': int(dt.strftime('%s'))
        }, conf.SECRET_KEY, algorithm='HS256')
    return token

def generate_access(phone: str):
    dt = datetime.now(timezone.utc) + timedelta(days=30)
    token = jwt.encode({
            'phone': phone,
            'exp': int(dt.strftime('%s'))
        }, conf.SECRET_KEY, algorithm='HS256')
    return token

def generate_stt(otp: int):
    dt = datetime.now() + timedelta(minutes = 3)
    token = jwt.encode({
            'otp': otp,
            'exp': int(dt.strftime('%s'))
        }, conf.SECRET_KEY, algorithm='HS256')
    return token

def decode(token: str):
    try:
        res = jwt.decode(token, conf.SECRET_KEY, algorithms=["HS256"])
        res['success'] = True
        return res
    
    except jwt.ExpiredSignatureError:
        return {"success":False, "status":"error", "message":"Token life time expired"}
    except:
        return {"success":False, "status":"error", "message":"Invalid token"}

import random

from auth.utils.kannelSMS import sendSMS
from fastapi import Header
from typing import Optional


def generate_otp(p_msisdn):
    '''for genereting and sendig sms to clients
    '''
    otp_value = str(random.randint(100000, 999999))
    sendSMS(p_msisdn, otp_value)
    print('------------------>', otp_value)
    return otp_value


def verify_access_token(authorization: Optional[str] = Header(default=None, alias='access-token')):
    token = authorization.strip()
    try:
        payload = jwt.decode(token, conf.SECRET_KEY, algorithms=["HS256"])
        phone = None
        if "sub" in payload:
            phone = payload.get("sub")
        elif "phone" in payload and isinstance(payload["phone"], dict):
            phone = payload["phone"].get("sub")
        if phone is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return phone
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def filtering(res):
    if res is not None and 'un_authorized' in res.keys():
        return JSONResponse(
            content={"message": "Not authorized"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    elif 'status' in res.keys() and res['status'] == 'error':
        return JSONResponse(
            content={"message": "Server error"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    else:
        return JSONResponse(
            content=res,
            status_code=status.HTTP_200_OK
        )