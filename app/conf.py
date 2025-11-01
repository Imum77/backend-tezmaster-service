from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY  = os.getenv("SECRET_KEY")

DB_USER     = os.getenv('DB_USER')
DB_PASS     = os.getenv('DB_PASS')
DB_HOST     = os.getenv('DB_HOST')

BILL_USERNAME        = os.getenv('BILL_USERNAME')
BILL_PASSWORD        = os.getenv('BILL_PASSWORD')
BILL_HOST            = os.getenv('BILL_HOST')
BILL_PORT            = os.getenv('BILL_PORT')
BILL_SERVICE_NAME    = os.getenv('BILL_SERVICE_NAME')