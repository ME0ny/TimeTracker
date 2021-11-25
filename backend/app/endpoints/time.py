from fastapi import APIRouter, Depends, Response
from repositories.time import TimeRepository
from .depends import get_time_repository, get_current_user
from models.user import User, UserIn
from models.time import Time, TimeIn
from typing import List

router = APIRouter()

@router.get("/", status_code=200, response_model=List[Time])
async def get_all_time(time: TimeRepository = Depends(get_time_repository), limit: int = 100, skip: int = 100):
    return await time.get_all(limit=limit, skip=0)

@router.post("/", status_code=250, response_model=Time)
async def create_user(
    response: Response,
    time_input: TimeIn,
    time: TimeRepository = Depends(get_time_repository)):
    resp = 250
    if await time.create(t=time_input) == None:
        resp = 251
    return Response(status_code=resp)

# @router.post("/say_hello", response_model=User)
# async def say_hello(
#     user: UserIn,
#     users: UserRepository = Depends(get_user_repository),
#     current_user: User = Depends(get_current_user)):
#     old_user = await users.get_by_login(login=user.login)
#     if old_user is None or old_user.login != current_user.login:
#         return HTTPException(status_code=404, detail="Not found user")
#     return old_user