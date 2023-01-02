from typing import Protocol
from uuid import UUID

from drivers.user_deletion import UserDeletionDriverProtocol


class UserDeletionServiceProtocol(Protocol):
    def delete(self, id: UUID) -> None:
        ...


class UserDeletionService:
    def __init__(self, driver: UserDeletionDriverProtocol) -> None:
        self.driver = driver

    def delete(self, id: UUID) -> None:
        self.driver.delete(id)
