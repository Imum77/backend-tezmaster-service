from pydantic import BaseModel, Field
from typing import Optional


class RequestRequest(BaseModel):
    offset  : Optional[int] = 0
    limit   : Optional[int] = 50


class StatusRequest(BaseModel):
       case_id     : str
       new_stat_id : str


class CommentRequest(BaseModel):
    comment          : Optional[str] = None
    upload_file      : Optional[str] = None
    case_id          : Optional[int] = None



class DeviceRequest(BaseModel):
       phone       : str = Field(min_length=12, max_length=12)
       ssid        : Optional[str]
       device      : Optional[str] = None 
       patch_cord  : Optional[str] = None 
       drop_cabel  : Optional[str] = None



class FindSubsRequest(BaseModel):
       fmsisdn  : str


class ReqDetailRequest(BaseModel):
       case_id  : int

class DelDeviceRequest(BaseModel):
       phone    : str = Field(min_length=12, max_length=12)
       case_id  : str

class ReqUserRequest(BaseModel):
       case_id      : str
       new_user_id  : str

class ReqStatusRequest(BaseModel):
       case_id      : str
       new_stat_id  : str

class AddDocumentRequest(BaseModel):
       case_id      : str
       comment      : str
       upload_file  : str
