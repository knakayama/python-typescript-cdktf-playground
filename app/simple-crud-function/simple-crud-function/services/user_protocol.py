from typing import Optional, Protocol
from uuid import UUID

from entities.user import User


class UserCreationProtocol(Protocol):
    def create(self, user: User) -> User:
        ...


class UserDescProtocol(Protocol):
    def describe(self, id: UUID) -> Optional[User]:
        ...


class UserUpdateProtocol(Protocol):
    def update(self) -> User:
        ...


class UserDeletionProtocol(Protocol):
    def delete(self) -> None:
        ...
