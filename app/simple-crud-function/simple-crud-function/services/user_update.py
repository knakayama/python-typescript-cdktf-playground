from typing import Protocol

from drivers.user_update import UserUpdateDriverProtocol
from entities.user import User
from use_cases.user_update import UserUpdateUseCaseInput


class UserUpdateServiceProtocol(Protocol):
    def update(self, input: UserUpdateUseCaseInput) -> User:
        ...


class UserUpdateService:
    def __init__(self, driver: UserUpdateDriverProtocol) -> None:
        self.driver = driver

    def update(self, input: UserUpdateUseCaseInput) -> User:
        return self.driver.update(User(**input.dict()))
