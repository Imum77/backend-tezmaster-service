from pydantic  import BaseModel
from typing    import Optional


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
       phone       : str
       ssid        : str
       device      : str
       patch_cord  : str
       drop_cabel  : str



class FindSubsRequest(BaseModel):
       fmsisdn  : str


class ReqDetailRequest(BaseModel):
       case_id  : int

class DelDeviceRequest(BaseModel):
       phone    : str
       case_id  : int

class ReqUserRequest(BaseModel):
       case_id      : int
       new_user_id  : int

class ReqStatusRequest(BaseModel):
       case_id      : str
       new_stat_id  : str

class AddDocumentRequest(BaseModel):
       case_id      : str
       comment      : str
       upload_file  : str
