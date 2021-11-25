from .users import UserRepository
from db.base import database
from typing import List, Optional
from models.user import User, UserIn

class UserRepositoryController:
    def __init__(self):
        self.user = UserRepository(database)

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        return await self.user.get_all(limit=limit, skip=skip)
    
    async def get_by_id(self, id: int) -> Optional[User]:
        return await self.user.get_by_id(id=id)

    async def get_by_login(self, login: str) -> User:
        return await self.user.get_by_login(login=login)

    async def get_by_hashId(self, hashId: str) -> User:
        return await self.user.get_by_hashId(hashId=hashId)
    
    async def create(self, u: UserIn) -> Optional[User]:
        return await self.user.create(u=u)
    
    async def update(self, id: int, hashId: str, u: UserIn):
        return await self.user.update(id=id, hashId=hash, u=u)
        
