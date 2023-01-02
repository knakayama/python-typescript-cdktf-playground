from typing import Protocol

from drivers.user import UserDriver
from entities.user import User
from pydash import omit


class UserCreationDriverProtocol(Protocol):
    def create(self, user: User) -> User:
        ...


class UserCreationDriver:
    def __init__(self, driver: UserDriver) -> None:
        self.driver = driver

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
