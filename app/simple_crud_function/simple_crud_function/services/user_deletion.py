from typing import Protocol
from uuid import UUID

from drivers.user_deletion import UserDeletionDriverProtocol


class UserDeletionServiceProtocol(Protocol):
    def delete(self, user_id: UUID) -> None:
        ...


class UserDeletionService:
    def __init__(self, user_deletion_driver: UserDeletionDriverProtocol) -> None:
        self.user_deletion_driver = user_deletion_driver

    def delete(self, user_id: UUID) -> None:
        self.user_deletion_driver.delete(user_id)
