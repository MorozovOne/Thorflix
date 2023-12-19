from dotenv import load_dotenv
import os

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

SMTP_USER = "abdullvagab123@gmail.com"
SMTP_PASS = "avkr lvey yeom uuuc"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

SECRET_KEY = os.environ.get('SECRET_KEY')

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:5432/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()