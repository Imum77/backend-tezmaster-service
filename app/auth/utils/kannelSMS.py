import aiohttp

async def sendSMS(msisdn, text, session: aiohttp.ClientSession):
    
    # host = "http://127.0.0.1:8007"
    host = "http://10.84.52.6:8007"
    url = (
        f"{host}/cgi-bin/sendsms?"
        f"username=mytcell&password=mytcell9&smsc=SMPPSim&to={msisdn}"
        f"&text={text}&from=MyTcell&coding=2&charset=UTF-8"
        )
    async with session.get(url) as resp:
        return resp.status == 202
