from .base import BaseRepository
from db.users import users
from typing import List, Optional
from models.user import User, UserIn
from core.security import hashed_password, hashed_id

class UserRepository(BaseRepository):
    
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
    
    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id==id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_login(self, login: str) -> User:
        query = users.select().where(users.c.login==login)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_hashId(self, hashId: str) -> User:
        query = users.select().where(users.c.hashId==hashId)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
    
    async def create(self, u: UserIn) -> Optional[User]:
        if not ((await self.get_by_login(u.login)) is None):
            return None
        user = User(
                hashId = hashed_id(u.login),
                login = u.login,
                hashed_password = hashed_password(u.password),
                first_name = u.first_name,
                last_name = u.last_name,
                status = u.status)
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id =  await self.database.execute(query)
        return user
    
    async def update(self, id: int, hashId: str, u: UserIn):
        user = User(
                id = id,
                hashId = hashId,
                login = u.login,
                hashed_password = hashed_password(u.password),
                first_name = u.first_name,
                last_name = u.last_name,
                status = u.status)
        values = {**user.dict()}
        values.pop("id", None)
        query = users.update().where(users.c.id==id).values(**values)
        await self.database.execute(query)
        return user
        