from typing import Protocol

from drivers.user_update import UserUpdateDriverProtocol
from entities.user import User
from use_cases.user_update import UserUpdateUseCaseInput


class UserUpdateServiceProtocol(Protocol):
    def update(self, input: UserUpdateUseCaseInput) -> User:
        ...


class UserUpdateService:
    def __init__(self, user_update_driver: UserUpdateDriverProtocol) -> None:
        self.user_update_driver = user_update_driver

    def update(self, input: UserUpdateUseCaseInput) -> User:
        return self.user_update_driver.update(User(**input.dict()))
