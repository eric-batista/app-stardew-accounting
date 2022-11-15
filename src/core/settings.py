import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

ROOT = Path(__file__).parent.parent


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
