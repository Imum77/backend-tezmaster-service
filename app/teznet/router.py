import oracledb
from fastapi            import APIRouter, Query, Depends, UploadFile, File, Form, Request
from db                 import get_db_conn
from teznet.crud        import (
                            get_user, get_requests, get_history, add_comment, add_device, 
                            find_subs, post_requests_detail, del_device, req_user, req_status,
                            add_document
                        )
from teznet.schemas     import (RequestRequest, CommentRequest, DeviceRequest, 
                           FindSubsRequest, ReqDetailRequest, DelDeviceRequest, ReqUserRequest, 
                           ReqStatusRequest, AddDocumentRequest
                        )
from auth.utils.utils   import verify_access_token

from auth.utils.utils import filtering

import json


router = APIRouter()


@router.get("/teznet/get-user/")
def get_user_by_msisdn(msisdn: str = Depends(verify_access_token)):
    res = get_user(msisdn = msisdn)
    return res

@router.get("/teznet/teznet-requests/")
def get_requests_by_msisdn(  
        data: RequestRequest = Query(...),
        msisdn: str = Depends(verify_access_token)
    ):
    res = get_requests(msisdn=msisdn, limit=data.limit, offset=data.offset)
    return filtering(res)

@router.get("/teznet/teznet-status/")
def get_status_by_msisdn(msisdn: str = Depends(verify_access_token)):
    res = get_history(msisdn=msisdn)
    return res

@router.post("/teznet/add-comment/")
async def add_comment_by_msisdn(data: CommentRequest, msisdn: str = Depends(verify_access_token)):
    return add_comment(msisdn=msisdn, case_id=data.case_id, comment=data.comment, upload_file=data.upload_file)

@router.post("/teznet/add-device/")
def add_device_by_msisdn(data: DeviceRequest, msisdn: str = Depends(verify_access_token)):
    return add_device(msisdn=msisdn, phone=data.phone, device=data.device, 
                      ssid=data.ssid, patch_cord=data.patch_cord, drop_cabel=data.drop_cabel
                    )

@router.post("/teznet/del-device/")
def delete_device(data: DelDeviceRequest, msisdn: str = Depends(verify_access_token)):
    return del_device(msisdn=msisdn, phone=data.phone, case_id=data.case_id)

@router.post("/teznet/find-subs/")
def find_subs_by_msisdn(data: FindSubsRequest, msisdn: str = Depends(verify_access_token)):
    return find_subs(msisdn=msisdn, fmsisdn=data.fmsisdn)

@router.post("/teznet/req-detail/")
async def request_detail(
        data: ReqDetailRequest,
        msisdn: str = Depends(verify_access_token),
        
    ):
    res = post_requests_detail(msisdn=msisdn, case_id=data.case_id)
    return res

@router.post("/teznet/change-req-user/")
def request_user(data: ReqUserRequest = Query(), msisdn: str = Depends(verify_access_token)):
    return req_user(msisdn=msisdn, case_id=data.case_id, new_user_id=data.new_user_id)

@router.post("/teznet/change-req-status/")
def request_status(data: ReqStatusRequest = Query(), msisdn: str = Depends(verify_access_token)):
    return req_status(msisdn=msisdn, case_id=data.case_id, new_stat_id=data.new_stat_id)


@router.post("/teznet/add-document/")
async def add_document_(
                        data: AddDocumentRequest, 
                        db: oracledb.AsyncConnection = Depends(get_db_conn), 
                        msisdn: str = Depends(verify_access_token)
                    ):
    return await add_document(db, msisdn=msisdn, case_id=data.case_id, comment=data.comment, upload_file=data.upload_file)
