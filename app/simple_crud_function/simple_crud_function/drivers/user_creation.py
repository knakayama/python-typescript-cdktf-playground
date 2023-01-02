from typing import Optional, Protocol

from drivers.user import UserDriver
from entities.user import User
from pydash import omit


class UserCreationDriverProtocol(Protocol):
    def create(self, user: User) -> User:
        ...


class UserCreationDriver:
    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def create(self, user: User) -> User:
        self.driver.table.put_item(
            Item={
                "pk": f"user#{user.id}",
                "sk": f"user#{user.id}",
                "gsi1": user.name,
                "id": f"{user.id}",
                **omit(user.dict(), "id"),
            },
            ConditionExpression=(
                "attribute_not_exists(#pk) AND attribute_not_exists(#sk)"
            ),
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )

        return user
