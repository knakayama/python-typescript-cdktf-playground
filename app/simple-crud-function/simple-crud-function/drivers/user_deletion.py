from typing import Optional, Protocol

from drivers.user import UserDriver
from services.user_deletion import UserDeletionServiceInput, UserDeletionServiceOutput
from typing_extensions import TypeAlias

UserDeletionDriverInput: TypeAlias = UserDeletionServiceInput
UserDeletionDriverOutput: TypeAlias = UserDeletionServiceOutput


class UserDeletionDriverProtocol(Protocol):
    def delete(self, input: UserDeletionDriverInput) -> UserDeletionDriverOutput:
        ...


class UserDeletionDriver:
    driver: UserDriver

    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def delete(self, input: UserDeletionDriverInput) -> UserDeletionDriverOutput:
        self.driver.table.delete_item(
            Key={
                "pk": f"user#{input}",
                "sk": f"user#{input}",
            },
            ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )
