from typing import Optional
from uuid import UUID
from drivers.user_protocol import UserDescDriverProtocol
from entities.user import User


class UserDescService:
    def __init__(self, driver: UserDescDriverProtocol) -> None:
        self.driver = driver

    def describe(self, id: UUID) -> Optional[User]:
        return self.driver.describe(id)
