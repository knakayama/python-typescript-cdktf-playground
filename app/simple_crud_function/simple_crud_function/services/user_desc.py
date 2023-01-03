from typing import Optional, Protocol
from uuid import UUID

from drivers.user_desc import UserDescDriverProtocol
from entities.user import User


class UserDescServiceProtocol(Protocol):
    def describe(self, user_id: UUID) -> Optional[User]:
        ...


class UserDescService:
    def __init__(self, user_desc_driver: UserDescDriverProtocol) -> None:
        self.user_desc_driver = user_desc_driver

    def describe(self, user_id: UUID) -> Optional[User]:
        return self.user_desc_driver.describe(user_id)
