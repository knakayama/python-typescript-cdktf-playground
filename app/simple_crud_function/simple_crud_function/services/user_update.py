from typing import Protocol

from drivers.user_update import UserUpdateDriverProtocol
from entities.user import User


class UserUpdateServiceProtocol(Protocol):
    def update(self, user: User) -> User:
        ...


class UserUpdateService:
    def __init__(self, user_update_driver: UserUpdateDriverProtocol) -> None:
        self.user_update_driver = user_update_driver

    def update(self, user: User) -> User:
        return self.user_update_driver.update(user)
