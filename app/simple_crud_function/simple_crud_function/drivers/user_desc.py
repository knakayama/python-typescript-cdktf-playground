from typing import Optional, Protocol
from uuid import UUID

from drivers.user import UserDriver
from entities.user import User


class UserDescDriverProtocol(Protocol):
    def describe(self, id: UUID) -> Optional[User]:
        ...


class UserDescDriver:
    def __init__(self, driver: UserDriver) -> None:
        self.driver = driver

    def describe(self, id: UUID) -> Optional[User]:
        output = self.driver.table.get_item(
            Key={
                "pk": f"user#{id}",
                "sk": f"user#{id}",
            },
        )

        if output.get("Item") is None:
            return None
        return User.parse_obj(output.get("Item"))
