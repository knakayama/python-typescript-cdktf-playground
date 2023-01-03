from typing import Protocol
from uuid import UUID

from botocore.exceptions import ClientError
from drivers.user import UserDriver
from exceptions.user import UserNotFound


class UserDeletionDriverProtocol(Protocol):
    def delete(self, user_id: UUID) -> None:
        ...


class UserDeletionDriver:
    user_driver: UserDriver

    def __init__(self, user_driver: UserDriver) -> None:
        self.user_driver = user_driver

    def delete(self, user_id: UUID) -> None:
        try:
            self.user_driver.table.delete_item(
                Key={
                    "pk": f"user#{user_id}",
                    "sk": f"user#{user_id}",
                },
                ConditionExpression="attribute_exists(#pk) AND attribute_exists(#sk)",
                ExpressionAttributeNames={
                    "#pk": "pk",
                    "#sk": "sk",
                },
            )
        except ClientError as error:
            if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
                raise UserNotFound(user_id)
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
