from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()


class Settings(BaseSettings):
    ENV: str
    BASE_PATH: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str

    class Config:
        case_sensitive = True


settings = Settings(
    ENV=os.getenv("ENV"),
    BASE_PATH=os.getenv("BASE_PATH"),
    DB_HOST=os.getenv("DB_HOST"),
    DB_USER=os.getenv("DB_USER"),
    DB_PASSWORD=os.getenv("DB_PASSWORD"),
)
