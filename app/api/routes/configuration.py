from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    if SECRET_KEY is None:
        raise ValueError("SECRET_KEY is missing")

    ALGORITHM: str = os.getenv('ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
