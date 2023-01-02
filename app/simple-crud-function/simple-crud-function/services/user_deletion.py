from typing import Protocol
from uuid import UUID

from drivers.user_deletion import UserDeletionDriverProtocol
from typing_extensions import TypeAlias

UserDeletionServiceInput: TypeAlias = UUID
UserDeletionServiceOutput: TypeAlias = None


class UserDeletionServiceProtocol(Protocol):
    def delete(self, input: UserDeletionServiceInput) -> UserDeletionServiceOutput:
        ...


class UserDeletionService:
    def __init__(self, driver: UserDeletionDriverProtocol) -> None:
        self.driver = driver

    def delete(self, input: UserDeletionServiceInput) -> UserDeletionServiceOutput:
        self.driver.delete(input)
