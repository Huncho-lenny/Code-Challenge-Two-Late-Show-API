import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "defaultjwtkey")
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URI environment variable not set")
