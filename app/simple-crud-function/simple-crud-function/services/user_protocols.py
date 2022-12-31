from typing import Optional, Protocol
from uuid import UUID

from entities.user import User


class UserCreationServiceProtocol(Protocol):
    def create(self, user: User) -> User:
        ...


class UserDescServiceProtocol(Protocol):
    def describe(self, id: UUID) -> Optional[User]:
        ...


class UserUpdateServiceProtocol(Protocol):
    def update(self, user: User) -> User:
        ...


class UserDeletionServiceProtocol(Protocol):
    def delete(self, id: UUID) -> None:
        ...
