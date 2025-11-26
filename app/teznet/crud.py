from fastapi import HTTPException
import requests, oracledb
import json
import aiohttp

async def get_user(msisdn: str, session: aiohttp.ClientSession):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=get_users&customer_msisdn={msisdn}"
        payload={}
        headers = {}

        async with session.post(url, data=payload, headers=headers) as response:
            res = await response.json()
            return res

    except Exception as e:
        return {
            "status": "error", 
            "message":"loyalty.db.history.get_history -> " + str(e)
            }
    
    
async def get_requests(session: aiohttp.ClientSession, msisdn, offset = 0, limit = 50):
    try:
        url = "http://10.84.33.83/gpon/cch/view.php?action=get_requests&customer_msisdn="+msisdn+"&offset="+str(offset)+"&limit="+str(limit)
        payload={}
        headers = {}

        async with session.post(url, headers=headers, data=payload) as response:
             res = await response.json()
             return res

    except Exception as e:
        return {
            "status": "error", 
            "message":"loyalty.db.history.get_history -> " + str(e)
            }

async def get_history(session: aiohttp.ClientSession, msisdn):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=get_status&customer_msisdn={msisdn}"
        payload={}
        headers = {}

        async with session.post(url, headers=headers, data = payload) as response:
            res = await response.json()
            return res

    except Exception as e:
        return {
            "status": "error", 
            "message":"loyalty.db.history.get_history -> " + str(e)
            }

async def add_comment(session: aiohttp.ClientSession, msisdn, case_id, comment, upload_file):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=add_comment&case_id={case_id}&customer_msisdn={msisdn}"
        payload={'comment': comment, 'upload_file': upload_file}
        headers = {}
            
        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
        
    except Exception as e:
        print(e)
        return {
            "status": "error", 
            "message":"teznet.db.teznet.find_subs -> " + str(e)
            }
    
async def add_device(session: aiohttp.ClientSession, msisdn, phone, device, ssid, patch_cord, drop_cabel):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=add_device&msisdn={phone}&device_number={device}&ssid={ssid}&patch_cord={patch_cord}&drop_cabel={drop_cabel}&customer_msisdn={msisdn}"
        payload=""
        headers = {}
            
        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.add_device -> " + str(e)
            }
    
async def find_subs(session: aiohttp.ClientSession, msisdn, fmsisdn):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=find_subs&customer_msisdn={msisdn}&msisdn={fmsisdn}"
        payload={}
        headers = {}

        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.find_subs -> " + str(e)
            }
    
async def post_requests_detail(session: aiohttp.ClientSession, msisdn, case_id):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=get_req_detail&case_id={case_id}&customer_msisdn={msisdn}"
        payload={}
        headers = {}

        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.request_detail -> " + str(e)
            }

async def del_device(session: aiohttp.ClientSession, msisdn, phone, case_id):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=del_device&msisdn={phone}&customer_msisdn={msisdn}&case_id={case_id}"
        payload=""
        headers = {}
            
        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.add_device -> " + str(e)
            }
    
async def req_user(session: aiohttp.ClientSession, msisdn, case_id, new_user_id):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=change_req_user&case_id={case_id}&new_user_id={new_user_id}&customer_msisdn={msisdn}"
        payload={'case_id': case_id, 'new_stat_id': new_user_id}
        headers = {}
        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.req_status -> " + str(e)
            }

async def req_status(session: aiohttp.ClientSession, msisdn, case_id, new_stat_id):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=change_req_status&case_id={case_id}&new_stat_id={new_stat_id}&customer_msisdn={msisdn}"
        payload={'case_id': case_id, 'new_stat_id': new_stat_id}
        headers = {}

        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.req_status -> " + str(e)
            }

async def add_document_cch(
        session: aiohttp.ClientSession, 
        url: str, 
        msisdn: str, 
        case_id: int, 
        comment: str, 
        upload_file: str
        ) -> requests.Response:
    payload = json.dumps({'comment': comment, 'upload_file':upload_file})
    headers = {}

    async with session.post(url, headers=headers, data=payload) as response:
        return await response.json()

async def add_document(
            db: oracledb.AsyncConnection, 
            session: aiohttp.ClientSession, 
            msisdn: str, 
            case_id: int, 
            comment: str, 
            upload_file: str
            ):

    url             = f"http://10.84.33.83/gpon/cch/view.php?action=add_document&case_id={case_id}&customer_msisdn={msisdn}"
    response_json   = await add_document_cch(session, url, msisdn, case_id, comment, upload_file)
    r_err_msg       = response_json.get('err_msg')

    cursor = db.cursor()

    try:
        o_result   = cursor.var(oracledb.NUMBER)
        o_err_msg  = cursor.var(oracledb.STRING)

        await cursor.callproc('log_mytcell_order', ('992934771005', url, str(response_json), r_err_msg , 'AddDocument', o_result, o_err_msg))
        
        result_code = o_result.getvalue()
        result_msg  = o_err_msg.getvalue()
        
        if result_code != 0:
             raise HTTPException(status_code=400, detail={'status': 'error', 'message': result_msg})
        return response_json

    except oracledb.DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        cursor.close()

async def add_device_alone(session: aiohttp.ClientSession, msisdn, phone, device, ssid, patch_cord, drop_cabel):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=add_device_bng_nce&msisdn={phone}&device_number={device}&ssid={ssid}&patch_cord={patch_cord}&drop_cabel={drop_cabel}&customer_msisdn={msisdn}"
        payload=""
        headers = {}

        async with session.post(url, headers=headers, data=payload) as response:
            res = await response.json()
            return res
    except Exception as e:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.add_device -> " + str(e)
            }
    
