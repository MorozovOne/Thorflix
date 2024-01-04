from typing import Optional


from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from auth.letter import send_letter_to_email
from auth.models import User, user
from auth.utils import get_user_db

from core.config import get_settings

SECRET = get_settings().get('secret_key')




class UserManager(IntegerIDMixin, BaseUserManager[user, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: user, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: user, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

        username = user.username
        email_str = user.email
        send_letter_to_email(token, username, email_str)


    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

        username = user.username
        email_str = user.email
        send_letter_to_email(token, username, email_str)




async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)