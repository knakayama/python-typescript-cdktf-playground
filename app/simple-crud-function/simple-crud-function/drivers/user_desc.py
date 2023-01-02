from typing import Optional, Protocol

from drivers.user import UserDriver
from entities.user import User
from services.user_desc import UserDescServiceInput, UserDescServiceOutput
from typing_extensions import TypeAlias

UserDescDriverInput: TypeAlias = UserDescServiceInput
UserDescDriverOutput: TypeAlias = UserDescServiceOutput


class UserDescDriverProtocol(Protocol):
    def describe(self, input: UserDescDriverInput) -> UserDescDriverOutput:
        ...


class UserDescDriver:
    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.driver = UserDriver(table_name=table_name, endpoint_url=endpoint_url)

    def describe(self, input: UserDescDriverInput) -> UserDescDriverOutput:
        output = self.driver.table.get_item(
            Key={
                "pk": f"user#{input}",
                "sk": f"user#{input}",
            },
        )

        if output.get("Item") is None:
            return None
        return User.parse_obj(output.get("Item"))
