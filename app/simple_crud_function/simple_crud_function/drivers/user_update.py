from typing import Protocol

from drivers.user import UserDriver
from entities.user import User


class UserUpdateDriverProtocol(Protocol):
    def update(self, user: User) -> User:
        ...


class UserUpdateDriver:
    def __init__(self, user_driver: UserDriver) -> None:
        self.user_driver = user_driver

    def update(self, user: User) -> User:
        self.user_driver.table.put_item(
            Item={
                "pk": f"user#{user.id}",
                "sk": f"user#{user.id}",
                "gsi1": user.name,
                "id": f"{user.id}",
                **user.dict(exclude={"id"}),
            },
            ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )

        return user
