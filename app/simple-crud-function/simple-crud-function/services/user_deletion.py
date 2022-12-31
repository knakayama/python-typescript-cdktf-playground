from uuid import UUID
from drivers.user_protocols import UserDeletionDriverProtocol


class UserDeletionService:
    def __init__(self, driver: UserDeletionDriverProtocol) -> None:
        self.driver = driver

    def delete(self, id: UUID) -> None:
        self.driver.delete(id)
