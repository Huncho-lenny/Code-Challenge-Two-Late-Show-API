import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("DATABASE_URI environment variable not set")
    if JWT_SECRET_KEY is None:
        raise ValueError("JWT_SECRET_KEY environment variable not set")