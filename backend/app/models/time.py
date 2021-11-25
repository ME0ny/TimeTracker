from pydantic import BaseModel, validator, constr
from typing import Optional
import datetime

class Time(BaseModel):
    id: Optional[int] = None
    hashId: str
    date: datetime.date
    time: int

class TimeIn(BaseModel):
    hashId: str
    time: Optional[int] = 0