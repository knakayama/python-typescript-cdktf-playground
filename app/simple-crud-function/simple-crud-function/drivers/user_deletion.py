from typing import Optional
from uuid import UUID

from drivers.user import UserDriver


class UserDeletionDriver:
    driver: UserDriver

    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def delete(self, id: UUID) -> None:
        self.driver.table.delete_item(
            Key={
                "pk": f"user#{id}",
                "sk": f"user#{id}",
            },
            ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
            ExpressionAttributeNames={
                "#pk": "pk",
                "#sk": "sk",
            },
        )
