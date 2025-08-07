from fastapi_users import schemas
from uuid import UUID
from typing import Optional

class UserRead(schemas.BaseUser[UUID]):
    first_name: str

class UserCreate(schemas.BaseUserCreate):
    first_name: str

class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str] = None
