from typing import Protocol

from drivers.user_creation import UserCreationDriverProtocol
from entities.user import User


class UserCreationServiceProtocol(Protocol):
    def create(self, user: User) -> User:
        ...


class UserCreationService:
    def __init__(self, user_creation_driver: UserCreationDriverProtocol) -> None:
        self.user_creation_driver = user_creation_driver

    def create(self, user: User) -> User:
        return self.user_creation_driver.create(user)
