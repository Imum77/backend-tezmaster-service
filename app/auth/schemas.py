from pydantic   import BaseModel, Field
from typing     import Optional, Literal
from datetime   import datetime


class OtpSchema(BaseModel):
    phone: str

class SttToken(BaseModel):
    stt: Optional[str] = None


class Verify(BaseModel):
    stt          : str
    otp          : str
    phone        : str = Field(min_length=12, max_length=12)
    device_model : str
    device_os    : str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    

class VerifyResponse(BaseModel):
    status: Optional[Literal['success', 'error']] = 'success'
    message: str = 'Token generated'
    data: Optional[TokenSchema] = None

class AuthOtpResponse(BaseModel):
    status  : Optional[Literal['success', 'error']] = 'success'
    message : Optional[str]                         = 'OTP sent with SMS'
    data    : Optional[SttToken]                    = None



class AuthHistoryResponse(BaseModel):
    id           :  int
    phone        :  str
    otp          :  str
    verified     :  bool
    create_date  :  datetime
    updated_date :  datetime
    device_os    :  Optional[str] = None
    token        :  str
    active       :  bool
    device_model :  Optional[str] = None
    device_ip    :  Optional[str] = None
    


class LogoutResponse(BaseModel):
    status  : Optional[Literal['success', 'error']] = 'success'
    message : str = "Logout success"