from os import environ, path
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_HOST = environ.get('DB_HOST')
    DB_NAME = environ.get('DB_NAME')
    DB_PORT = environ.get('DB_PORT')

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY','rbjfr43r3rnke39dw')
    LOG_FILE = environ.get('LOG_FILE','logs/app.log')
    LOG_LEVEL='INFO'