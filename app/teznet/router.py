import oracledb
from fastapi              import APIRouter, Query, Depends, Form
import aiohttp
from db                   import get_db_conn
from teznet.crud          import (
                                get_user, get_requests, get_history, add_comment,
                                find_subs, post_requests_detail, del_device, req_user, req_status,
                                add_document, add_device_alone
                            )
from teznet.schemas       import (
                                RequestRequest, CommentRequest, DeviceRequest, 
                                FindSubsRequest, ReqDetailRequest, DelDeviceRequest, ReqUserRequest, 
                                ReqStatusRequest, AddDocumentRequest
                                )
from auth.utils.utils     import verify_access_token
from dependencies.session import get_http_session

router = APIRouter()


@router.get("/teznet/get-user/")
async def get_user_by_msisdn(
        msisdn: str = Depends(verify_access_token), 
        session: aiohttp.ClientSession = Depends(get_http_session)
    ):
    res = await get_user(msisdn = msisdn, session = session)
    return res

@router.get("/teznet/teznet-requests/")
async def get_requests_by_msisdn(  
        data: RequestRequest = Query(...),
        msisdn: str = Depends(verify_access_token),
        session: aiohttp.ClientSession = Depends(get_http_session)
    ):
    res = await get_requests(msisdn=msisdn, limit=data.limit, offset=data.offset, session=session)
    return res



@router.get("/teznet/teznet-status/")
async def get_status_by_msisdn(
        msisdn: str = Depends(verify_access_token),
        session: aiohttp.ClientSession = Depends(get_http_session)
        ):
    res = await get_history(msisdn=msisdn, session=session)
    return res

@router.post("/teznet/add-comment/")
async def add_comment_by_msisdn(
            data: CommentRequest, 
            msisdn: str = Depends(verify_access_token),
            session: aiohttp.ClientSession = Depends(get_http_session)
        ):
    res = await add_comment(
            msisdn=msisdn, 
            case_id=data.case_id, 
            comment=data.comment, 
            upload_file=data.upload_file, 
            session=session
        )
    return res

@router.post("/teznet/add-device/")
async def add_device_by_msisdn(
            data: DeviceRequest, 
            msisdn: str = Depends(verify_access_token),
            session: aiohttp.ClientSession = Depends(get_http_session)
        ):
    # if msisdn == '992112212222':
    res = await add_device_alone(
                msisdn=msisdn, 
                phone=data.phone, 
                device=data.device, 
                ssid=data.ssid, 
                patch_cord=data.patch_cord, 
                drop_cabel=data.drop_cabel,
                session=session
                            )
        # return res
               
    return res

@router.post("/teznet/del-device/")
async def delete_device(
        data: DelDeviceRequest, 
        msisdn: str = Depends(verify_access_token),
        session: aiohttp.ClientSession = Depends(get_http_session)
        ):
    res = await del_device(
        msisdn=msisdn, 
        phone=data.phone, 
        case_id=data.case_id, 
        session=session
        )
    return res

@router.post("/teznet/find-subs/")
async def find_subs_by_msisdn(
        data: FindSubsRequest, 
        msisdn: str = Depends(verify_access_token),
        session: aiohttp.ClientSession = Depends(get_http_session)
        ):
    res = await find_subs(msisdn=msisdn, fmsisdn=data.fmsisdn, session=session)
    return res

@router.post("/teznet/req-detail/")
async def request_detail(
        data: ReqDetailRequest,
        msisdn: str = Depends(verify_access_token),
        session: aiohttp.ClientSession = Depends(get_http_session)    
    ):
    res = await post_requests_detail(msisdn=msisdn, case_id=data.case_id, session=session)
    return res

@router.post("/teznet/change-req-user/")
async def request_user(
    data: ReqUserRequest, 
    msisdn: str = Depends(verify_access_token),
    session: aiohttp.ClientSession = Depends(get_http_session)
    ):
    res = await req_user(
        msisdn=msisdn, 
        case_id=data.case_id, 
        new_user_id=data.new_user_id, 
        session=session
        )
    return res

@router.post("/teznet/change-req-status/")
async def request_status(
        data: ReqStatusRequest,     
        msisdn: str = Depends(verify_access_token),
        session: aiohttp.ClientSession = Depends(get_http_session)
        ):
    res = await req_status(
        msisdn=msisdn, 
        case_id=data.case_id, 
        new_stat_id=data.new_stat_id,
        session=session
        )
    return res


@router.post("/teznet/add-document/")
async def add_document_(
                        data: AddDocumentRequest = Form(...), 
                        db: oracledb.AsyncConnection = Depends(get_db_conn), 
                        session: aiohttp.ClientSession = Depends(get_http_session),
                        msisdn: str = Depends(verify_access_token)
                    ):
    res = await add_document(
            db, 
            session,
            msisdn=msisdn, 
            case_id=data.case_id, 
            comment=data.comment, 
            upload_file=data.upload_file,
            )
    return res 


