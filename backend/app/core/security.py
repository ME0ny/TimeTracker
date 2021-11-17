from passlib.context import CryptContext
from jose import jwt
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
import datetime
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password: str) -> str:
    return pwd_context.hash(password)

def hashed_id(login: str) -> str:
    return pwd_context.hash(login + str(datetime.datetime.now()))

def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)