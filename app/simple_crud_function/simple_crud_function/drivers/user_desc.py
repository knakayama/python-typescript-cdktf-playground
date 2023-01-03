from typing import Optional, Protocol
from uuid import UUID

from drivers.user import UserDriver
from entities.user import User


class UserDescDriverProtocol(Protocol):
    def describe(self, user_id: UUID) -> Optional[User]:
        ...


class UserDescDriver:
    def __init__(self, user_driver: UserDriver) -> None:
        self.user_driver = user_driver

    def describe(self, user_id: UUID) -> Optional[User]:
        output = self.user_driver.table.get_item(
            Key={
                "pk": f"user#{user_id}",
                "sk": f"user#{user_id}",
            },
        )

        if output.get("Item") is None:
            return None
        return User.parse_obj(output.get("Item"))
