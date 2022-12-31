from typing import Optional
from uuid import UUID

from drivers.user import UserDriver
from entities.user import User


class UserDescDriver:
    driver: UserDriver

    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

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