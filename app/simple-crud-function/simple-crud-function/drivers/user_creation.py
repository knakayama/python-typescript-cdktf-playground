from typing import Optional

from drivers.user import UserDriver
from entities.user import User
from pydash import omit


class UserCreationDriver:
    driver: UserDriver

    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def create(self, user: User) -> User:
        new_user = User(**omit(user.dict(), "name"))

        self.driver.table.put_item(
            Item={
                "pk": f"user#{new_user.id}",
                "sk": f"user#{new_user.id}",
                "gsi1": new_user.name,
                "id": f"{new_user.id}",
                **omit(new_user.dict(), "id"),
            },
            ConditionExpression=(
                "attribute_not_exists(#pk) AND attribute_not_exists(#sk)"
            ),
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )

        return new_user
