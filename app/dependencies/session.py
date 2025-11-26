import aiohttp
 
HTTP_SESSION = None

async def get_http_session():
    global HTTP_SESSION
    if HTTP_SESSION is None:
        HTTP_SESSION = aiohttp.ClientSession()
    try:
        yield HTTP_SESSION
    finally:
        pass