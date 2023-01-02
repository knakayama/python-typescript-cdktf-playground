from typing import Optional, Protocol

from drivers.user import UserDriver
from entities.user import User
from pydash import omit


class UserUpdateDriverProtocol(Protocol):
    def update(self, user: User) -> User:
        ...


class UserUpdateDriver:
    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def update(self, user: User) -> User:
        self.driver.table.put_item(
            Item={
                "pk": f"user#{user.id}",
                "sk": f"user#{user.id}",
                "gsi1": user.name,
                "id": f"{user.id}",
                **omit(user.dict(), "id"),
            },
            ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )

        return user
