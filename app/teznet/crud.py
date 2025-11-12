import requests, sys, oracledb
from fastapi import HTTPException

def get_user(msisdn: str):
    try:
        url = f"http://10.84.33.83/gpon/cch/view.php?action=get_users&customer_msisdn={msisdn}"
        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data = payload)
        res=response.json()
        return res

    except:
        return {
            "status": "error", 
            "message":"loyalty.db.history.get_history -> " + str(sys.exc_info()[1])
            }
    
def get_requests(msisdn, offset = 0, limit = 15):
    try:
        print('offset ', offset)
        print('limit ', limit)


        url = "http://10.84.33.83/gpon/cch/view.php?action=get_requests&customer_msisdn="+msisdn+"&offset="+str(offset)+"&limit="+str(limit)

        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data = payload)
        res=response.json()
        return res

    except:
        return {
            "status": "error", 
            "message":"loyalty.db.history.get_history -> " + str(sys.exc_info()[1])
            }
    

def get_history(msisdn):
    print('------------->', msisdn)
    try:
        url = "http://10.84.33.83/gpon/cch/view.php?action=get_status&customer_msisdn="+msisdn+""
        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data = payload)
        res=response.json()
        print(res)
        return res

    except:
        return {
            "status": "error", 
            "message":"loyalty.db.history.get_history -> " + str(sys.exc_info()[1])
            }


def add_comment(msisdn, case_id, comment, upload_file):
    try:

            url = "http://10.84.33.83/gpon/cch/view.php?action=add_comment&case_id="+case_id+"&customer_msisdn="+msisdn+""
            payload={'comment': comment,
                    'upload_file': upload_file}
            headers = {}
            
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.find_subs -> " + str(sys.exc_info()[1])
            }
    
def add_device(msisdn, phone, device, ssid, patch_cord, drop_cabel):
    try:

            url = "http://10.84.33.83/gpon/cch/view.php?action=add_device&msisdn="+phone+"&device_number="+device+"&ssid="+ssid+"&patch_cord="+patch_cord+"&drop_cabel="+drop_cabel+"&customer_msisdn="+msisdn+""
            payload=""
            headers = {}
            
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.add_device -> " + str(sys.exc_info()[1])
            }
    
def find_subs(msisdn, fmsisdn):
    try:

            url = "http://10.84.33.83/gpon/cch/view.php?action=find_subs&customer_msisdn="+msisdn+"&msisdn="+fmsisdn+""
            payload={}
            headers = {}
            
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.find_subs -> " + str(sys.exc_info()[1])
            }
    

def post_requests_detail(msisdn, case_id):
    try:

            url = f"http://10.84.33.83/gpon/cch/view.php?action=get_req_detail&case_id={case_id}&customer_msisdn={msisdn}"
            payload={}
            headers = {}
            
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.request_detail -> " + str(sys.exc_info()[1])
            }


def del_device(msisdn, phone, case_id):
    try:
            url = "http://10.84.33.83/gpon/cch/view.php?action=del_device&msisdn="+phone+"&customer_msisdn="+msisdn+"&case_id="+case_id+""
            payload=""
            headers = {}
            
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.add_device -> " + str(sys.exc_info()[1])
            }
    
def req_user(msisdn, case_id, new_user_id):
    try:
            url = "http://10.84.33.83/gpon/cch/view.php?action=change_req_user&case_id="+case_id+"&new_user_id="+new_user_id+"&customer_msisdn="+msisdn+""
            payload={'case_id': case_id,
                    'new_stat_id': new_user_id}
            headers = {}
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.req_status -> " + str(sys.exc_info()[1])
            }

def req_status(msisdn, case_id, new_stat_id):
    try:

            url = "http://10.84.33.83/gpon/cch/view.php?action=change_req_status&case_id="+case_id+"&new_stat_id="+new_stat_id+"&customer_msisdn="+msisdn+""
            payload={'case_id': case_id,
                    'new_stat_id': new_stat_id}
            headers = {}
            
            response = requests.request('POST', url, headers=headers, data=payload)
            res = response.json()
            return res
    except:
        return {
            "status": "error", 
            "message":"teznet.db.teznet.req_status -> " + str(sys.exc_info()[1])
            }


import json

async def add_document_cch(url: str, msisdn: str, case_id: int, comment: str, upload_file: str) -> requests.Response:
    payload = json.dumps({'comment': comment, 'upload_file':upload_file})
    return requests.request('POST', url, headers={}, data=payload)


async def add_document(db: oracledb.AsyncConnection, msisdn: str, case_id: int, comment: str, upload_file: str):

    url             = "http://10.84.33.83/gpon/cch/view.php?action=add_document&case_id="+case_id+"&customer_msisdn="+msisdn+""
    response        = await add_document_cch(url, msisdn, case_id, comment, upload_file)
    response_json   = response.json()
    r_err_msg       = response_json.get('err_msg')

    cursor = db.cursor()

    try:
        o_result   = cursor.var(oracledb.NUMBER)
        o_err_msg  = cursor.var(oracledb.STRING)

        await cursor.callproc('log_mytcell_order', ('992777003304', url, str(response_json), r_err_msg , 'AddDocument', o_result, o_err_msg))
        
        result_code = o_result.getvalue()
        result_msg  = o_err_msg.getvalue()
        
        if result_code != 0:
             raise HTTPException(status_code=400, detail={'status': 'error', 'message': result_msg})
        print(response_json)
        return response_json

    except oracledb.DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        cursor.close()