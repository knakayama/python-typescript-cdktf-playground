from typing import Optional

from drivers.user import UserDriver
from entities.user import User
from pydash import omit
from services.user_creation import UserCreationServiceOutput
from typing_extensions import TypeAlias

UserCreationDriverInput: TypeAlias = User
UserCreationDriverOutput: TypeAlias = UserCreationServiceOutput


class UserCreationDriver:
    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def create(self, input: UserCreationDriverInput) -> UserCreationDriverOutput:
        self.driver.table.put_item(
            Item={
                "pk": f"user#{input.id}",
                "sk": f"user#{input.id}",
                "gsi1": input.name,
                "id": f"{input.id}",
                **omit(input.dict(), "id"),
            },
            ConditionExpression=(
                "attribute_not_exists(#pk) AND attribute_not_exists(#sk)"
            ),
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )

        return input
