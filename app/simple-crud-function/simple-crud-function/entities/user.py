from typing import Optional, cast
from uuid import uuid4

from modules.type_hints import CountryCode
from modules.user import to_name
from pydantic import UUID4, BaseModel, EmailStr, Field
from validators.user import (
    UserAddress,
    UserAge,
    UserFirstAndLastName,
    UserName,
    UserZipCode,
)


class User(BaseModel):
    first_name: UserFirstAndLastName
    middle_name: Optional[UserFirstAndLastName]
    last_name: UserFirstAndLastName
    age: UserAge
    address: UserAddress
    zip_code: UserZipCode
    country: CountryCode
    # TODO: The filed below should not be None
    name: Optional[UserName]
    id: UUID4 = Field(default_factory=uuid4)
    email: EmailStr

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.name = cast(
            UserName,
            to_name(self.first_name, self.middle_name, self.last_name),
        )
