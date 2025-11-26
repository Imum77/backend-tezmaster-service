from fastapi        import FastAPI
from auth.router    import router as auth_router
from teznet.router  import router as teznet_router

app = FastAPI(
    title="GPON API",
    description="API для получения информации о пользователях GPON",
    version="1.0.0",
    debug=True
)

app.include_router(auth_router, tags=["Authorization"]  , prefix='/api/v3')
app.include_router(teznet_router, tags=["TezNet"] , prefix='/api/v3')

