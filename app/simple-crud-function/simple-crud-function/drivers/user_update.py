from typing import Optional, Protocol

from drivers.user import UserDriver
from entities.user import User
from pydash import omit
from services.user_update import UserUpdateServiceInput, UserUpdateServiceOutput
from typing_extensions import TypeAlias

UserUpdateDriverInput: TypeAlias = UserUpdateServiceInput
UserUpdateDriverOutput: TypeAlias = UserUpdateServiceOutput


class UserUpdateDriverProtocol(Protocol):
    def update(self, input: UserUpdateDriverInput) -> UserUpdateDriverOutput:
        ...


class UserUpdateDriver:
    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def update(self, input: UserUpdateDriverInput) -> UserUpdateDriverOutput:
        updated_user = User(**omit(input.dict(), "name"))

        self.driver.table.put_item(
            Item={
                "pk": f"user#{updated_user.id}",
                "sk": f"user#{updated_user.id}",
                "gsi1": updated_user.name,
                "id": f"{updated_user.id}",
                **omit(updated_user.dict(), "id"),
            },
            ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )

        return updated_user
