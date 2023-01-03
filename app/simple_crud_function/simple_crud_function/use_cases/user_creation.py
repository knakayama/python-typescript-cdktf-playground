from typing import Optional

from entities.user import User
from modules.type_hints import CountryCode
from pydantic import BaseModel, EmailStr
from services.user_creation import UserCreationServiceProtocol
from validators.constraints.user import (
    UserAddress,
    UserAge,
    UserFirstAndLastName,
    UserZipCode,
)


class UserCreationUseCaseInput(BaseModel):
    first_name: UserFirstAndLastName
    middle_name: Optional[UserFirstAndLastName]
    last_name: UserFirstAndLastName
    age: UserAge
    address: UserAddress
    zip_code: UserZipCode
    country: CountryCode
    email: EmailStr


class UserCreationUseCase:
    def __init__(self, user_creation_service: UserCreationServiceProtocol) -> None:
        self.user_creation_service = user_creation_service

    def execute(self, input: UserCreationUseCaseInput) -> User:
        return self.user_creation_service.create(input)
