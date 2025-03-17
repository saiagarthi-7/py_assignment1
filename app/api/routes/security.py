from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from .configuration import settings
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hash(password: str):
    return pwd_context.hash(password)

def pass_verify(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expires_delta: timedelta = None):
    to_encode = {"sub": subject}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def decode_token(token: str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return data
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token or token expired")

