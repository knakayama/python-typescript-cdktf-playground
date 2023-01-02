from typing import Optional, Protocol
from uuid import UUID

from drivers.user_desc import UserDescDriverProtocol
from entities.user import User


class UserDescServiceProtocol(Protocol):
    def describe(self, id: UUID) -> Optional[User]:
        ...


class UserDescService:
    def __init__(self, driver: UserDescDriverProtocol) -> None:
        self.driver = driver

    def describe(self, id: UUID) -> Optional[User]:
        return self.driver.describe(id)
