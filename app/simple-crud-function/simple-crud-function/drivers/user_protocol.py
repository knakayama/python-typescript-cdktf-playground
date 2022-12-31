from typing import Optional, Protocol
from uuid import UUID

from entities.user import User


class UserCreationDriverProtocol(Protocol):
    def create(self, user: User) -> User:
        ...


class UserDescDriverProtocol(Protocol):
    def describe(self, id: UUID) -> Optional[User]:
        ...


class UserUpdateDriverProtocol(Protocol):
    def update(self, user: User) -> User:
        ...


class UserDeletionDriverProtocol(Protocol):
    def delete(self, id: UUID) -> None:
        ...
