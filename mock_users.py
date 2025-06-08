import json
from random import choice
from pydantic import BaseModel, EmailStr, ValidationError


class User(BaseModel):
    username: str
    name: str | None
    last_name: str | None
    email: EmailStr


class MockUsers:

    def __init__(self, source):
        self.source = source

    def get_user(self) -> User:
        with open(self.source, "r", encoding="utf-8") as file:
            data = json.load(file)
            return User.model_validate(choice(data))




