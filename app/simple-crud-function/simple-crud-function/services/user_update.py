from typing import Protocol

from drivers.user_update import UserUpdateDriverProtocol
from entities.user import User
from typing_extensions import TypeAlias

UserUpdateServiceInput: TypeAlias = User
UserUpdateServiceOutput: TypeAlias = User


class UserUpdateServiceProtocol(Protocol):
    def update(self, input: UserUpdateServiceInput) -> UserUpdateServiceOutput:
        ...


class UserUpdateService:
    def __init__(self, driver: UserUpdateDriverProtocol) -> None:
        self.driver = driver

    def update(self, input: UserUpdateServiceInput) -> UserUpdateServiceOutput:
        return self.driver.update(input)
