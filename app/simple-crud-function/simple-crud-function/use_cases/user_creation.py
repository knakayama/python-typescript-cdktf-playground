from typing import Optional

from entities.user import User
from modules.type_hints import CountryCode
from pydantic import BaseModel, EmailStr
from services.user_creation import UserCreationService
from typing_extensions import TypeAlias
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


UserCreationUseCaseOutput: TypeAlias = User


class UserCreationUseCase:
    def __init__(self, service: UserCreationService) -> None:
        self.service = service

    def execute(self, input: UserCreationUseCaseInput) -> UserCreationUseCaseOutput:
        return self.service.create(input)
