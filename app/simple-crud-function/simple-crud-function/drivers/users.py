from typing import Protocol

from entities.user import User


class UsersProtocol(Protocol):
    def list(self) -> list[User]:
        ...
