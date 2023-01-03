from typing import Protocol

from drivers.user_creation import UserCreationDriverProtocol
from entities.user import User
from use_cases.user_creation import UserCreationUseCaseInput


class UserCreationServiceProtocol(Protocol):
    def create(self, input: UserCreationUseCaseInput) -> User:
        ...


class UserCreationService:
    def __init__(self, user_creation_driver: UserCreationDriverProtocol) -> None:
        self.user_creation_driver = user_creation_driver

    def create(self, input: UserCreationUseCaseInput) -> User:
        return self.user_creation_driver.create(User(**input.dict()))
