from .base import BaseRepository
from db.time import time
from models.time import Time, TimeIn
from core.security import hashed_password, hashed_id
from .interface_users import UserRepositoryController
from typing import List, Optional
import datetime

class TimeRepository(BaseRepository):
    
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Time]:
        query = time.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
    
    async def get_by_id(self, id: int) -> Optional[Time]:
        query = time.select().where(time.c.id==id)
        item_time = await self.database.fetch_one(query)
        if item_time is None:
            return None
        return Time.parse_obj(item_time)

    async def get_by_hashId(self, hashId: str) -> List[Time]:
        query = time.select().where(time.c.hashId==hashId)
        item_time = await self.database.fetch_one(query)
        if item_time is None:
            return None
        return item_time
    
    async def get_by_hashId_and_date(self, hashId: str, date: datetime.date) -> Time:
        query = time.select().where(time.c.hashId==hashId).where(time.c.date==date)
        item_time = await self.database.fetch_one(query)
        if item_time is None:
            return None
        return Time.parse_obj(item_time)
    
    async def create(self, t: TimeIn) -> Optional[Time]:
        if not ((await self.get_by_hashId_and_date(hashId=t.hashId, date=datetime.datetime.now().date())) is None):
            return None
        user = UserRepositoryController()
        if await user.get_by_hashId(t.hashId) is None:
            return None
        del user
        item_time = Time(
            hashId = t.hashId,
            date = datetime.datetime.now().date(),
            time = t.time)
        values = {**item_time.dict()}
        values.pop("id", None)
        query = time.insert().values(**values)
        item_time.id =  await self.database.execute(query)
        return item_time
    
    async def update(self, t: TimeIn) -> TimeIn:
        if not ((await self.get_by_hashId_and_date(hashId=t.hashId, date=datetime.datetime.now().date())) is None):
            return None
        user = UserRepositoryController()
        if user.get_by_hashId(t.hashId) is None:
            return None
        del user
        item_time = Time(
            hashId = t.hashId,
            date = datetime.datetime.now().date(),
            time = t.time)
        values = {**item_time.dict()}
        values.pop("id", None)
        query = time.update().where(time.c.hashId==item_time.hashId).where(time.c.date==item_time.date).values(**values)
        await self.database.execute(query)
        return item_time