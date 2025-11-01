import  logging
import  oracledb
from    sqlalchemy      import create_engine
from    sqlalchemy.orm  import sessionmaker
import  conf as conf


logger = logging.getLogger(__name__)

DATABASE_URL = f"mysql+pymysql://{conf.DB_USER}:{conf.DB_PASS}@{conf.DB_HOST}/my_tcell_lite_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



dsn = oracledb.makedsn(conf.BILL_HOST, conf.BILL_PORT, service_name=conf.BILL_SERVICE_NAME)
POOL = None

async def init_db():
    global POOL
    if POOL is None:
        logger.info("Initializing Oracle DB connection pool...")
        POOL = oracledb.create_pool_async(
            user=conf.BILL_USERNAME,
            password=conf.BILL_PASSWORD,
            dsn=dsn,
            min=1,
            max=5,
            increment=1,
            timeout=300,
            max_lifetime_session=1800
        )
        logger.info("Oracle DB connection pool initialized.")

async def close_db():
    global POOL
    if POOL is not None:
        logger.info("Closing Oracle DB connection pool...")
        await POOL.close()
        POOL = None
        logger.info("Oracle DB connection pool closed.")

async def get_db_conn():
    if POOL is None:
        await init_db()
    connection = await POOL.acquire()
    try:
        yield connection
    finally:
        await POOL.release(connection)