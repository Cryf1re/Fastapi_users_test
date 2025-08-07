from fastapi_users.manager import BaseUserManager
from app.config import get_settings
from app.models.user import User
from fastapi import Request, Response
from typing import Optional
from uuid import UUID
import uuid

settings = get_settings()


class UserManager(BaseUserManager[User, uuid.UUID]):
    user_db_model = User
    reset_password_token_secret = settings.secret
    verification_token_secret = settings.secret

    def parse_id(self, id_str: str) -> UUID:
        return UUID(id_str)

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        print(f"User {user.id} registered.")

    async def on_after_login(
    self,
    user: User,
    request: Optional[Request] = None,
    response: Optional[Response] = None,
) -> None:
        print(f"User {user.id} logged in.")