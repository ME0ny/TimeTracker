from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from .depends import get_user_repository
from models.user import User, UserIn
from typing import List

router = APIRouter()

@router.get("/", status_code=200, response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 100):
    return await users.get_all(limit=limit, skip=0)

@router.post("/", status_code=200, response_model=User)
async def create(
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)