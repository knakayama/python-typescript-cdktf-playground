from typing import Optional

from entities.user import User
from modules.type_hints import CountryCode
from pydantic import UUID4, BaseModel, EmailStr
from services.user_update import UserUpdateServiceProtocol
from validators.constraints.user import (
    UserAddress,
    UserAge,
    UserFirstAndLastName,
    UserZipCode,
)


class UserUpdateUseCaseInput(BaseModel):
    first_name: UserFirstAndLastName
    middle_name: Optional[UserFirstAndLastName]
    last_name: UserFirstAndLastName
    age: UserAge
    address: UserAddress
    zip_code: UserZipCode
    country: CountryCode
    email: EmailStr
    id: UUID4


class UserUpdateUseCase:
    def __init__(self, service: UserUpdateServiceProtocol) -> None:
        self.service = service

    def execute(self, input: UserUpdateUseCaseInput) -> User:
        return self.service.update(input)
