from pydantic import BaseModel, Field

class RequestRequest(BaseModel):
    offset  : str
    limit   : str


class StatusRequest(BaseModel):
       case_id     : str
       new_stat_id : str


class CommentRequest(BaseModel):
       case_id     : str
       comment     : str
       upload_file : str



class DeviceRequest(BaseModel):
       phone       : str = Field(min_length=12, max_length=12)
       device      : str 
       ssid        : str 
       patch_cord  : str 
       drop_cabel  : str



class FindSubsRequest(BaseModel):
       fmsisdn  : str


class ReqDetailRequest(BaseModel):
       case_id  : str

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