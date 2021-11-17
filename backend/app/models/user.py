from pydantic import BaseModel, validator, constr
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    hashId: str
    login: str
    hashed_password: str
    first_name: str
    last_name: str
    status: str

class UserIn(BaseModel):
    login: str
    first_name: str
    last_name: str
    status: str
    password: constr(min_length=8, max_length=16)
    password2: str

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("password don't match")
        return v