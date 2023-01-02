from random import choice
from typing import Optional, cast
from uuid import UUID, uuid4

from entities.user import User
from faker import Faker
from modules.type_hints import CountryCode

fake = Faker()


def string() -> str:
    return cast(str, fake.pystr())


def first_name() -> str:
    return cast(str, fake.first_name())


def last_name() -> str:
    return cast(str, fake.last_name())


def address() -> str:
    return cast(str, fake.address())


def zip_code() -> str:
    return cast(str, fake.postcode())


def country_code() -> CountryCode:
    return choice(["JPN", "PHL", "USA"])


def age() -> int:
    return cast(int, fake.pyint(max_value=100))


def user_id() -> UUID:
    return uuid4()


def email() -> str:
    return cast(str, fake.email())


def user(middle_name: Optional[str] = None) -> User:
    return User(
        first_name=first_name(),
        last_name=last_name(),
        middle_name=middle_name,
        address=address(),
        zip_code=zip_code(),
        country=country_code(),
        age=age(),
        email=email(),
    )
