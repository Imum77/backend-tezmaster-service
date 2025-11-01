
from fastapi        import FastAPI, HTTPException
from auth.router    import router as auth_router
from teznet.router  import router as teznet_router

app = FastAPI(
    title="GPON API",
    description="API для получения информации о пользователях GPON",
    version="1.0.0"
)

app.include_router(auth_router, tags=["auth"])
app.include_router(teznet_router, tags=["cab"])

