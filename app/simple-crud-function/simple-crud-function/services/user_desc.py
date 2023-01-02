from typing import Optional, Protocol
from uuid import UUID

from drivers.user_desc import UserDescDriverProtocol
from entities.user import User
from typing_extensions import TypeAlias

UserDescServiceInput: TypeAlias = UUID
UserDescServiceOutput: TypeAlias = Optional[User]


class UserDescServiceProtocol(Protocol):
    def describe(self, input: UserDescServiceInput) -> UserDescServiceOutput:
        ...


class UserDescService:
    def __init__(self, driver: UserDescDriverProtocol) -> None:
        self.driver = driver

    def describe(self, input: UserDescServiceInput) -> UserDescServiceOutput:
        return self.driver.describe(input)
