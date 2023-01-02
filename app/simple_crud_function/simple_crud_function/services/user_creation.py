from typing import Protocol

from drivers.user_creation import UserCreationDriverProtocol
from entities.user import User
from use_cases.user_creation import UserCreationUseCaseInput


class UserCreationServiceProtocol(Protocol):
    def create(self, input: UserCreationUseCaseInput) -> User:
        ...


class UserCreationService:
    def __init__(self, driver: UserCreationDriverProtocol) -> None:
        self.driver = driver

    def create(self, input: UserCreationUseCaseInput) -> User:
        return self.driver.create(User(**input.dict()))
