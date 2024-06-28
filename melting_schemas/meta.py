from typing import NotRequired, TypedDict

from pydantic import EmailStr


class Creator(TypedDict):
    client_name: str
    token_name: str
    user_email: EmailStr
    user_ip: NotRequired[str]
