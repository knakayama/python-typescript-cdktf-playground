from typing import Generator

import pytest
from drivers.user import UserDriver
from drivers.user_creation import UserCreationDriver
from drivers.user_deletion import UserDeletionDriver
from drivers.user_desc import UserDescDriver
from drivers.user_update import UserUpdateDriver

from tests.unit.constants import endpoint_url, table_name
from tests.unit.fixtures.table import TableFixture

table = TableFixture(table_name=table_name, endpoint_url=endpoint_url)


@pytest.fixture(scope="session", autouse=True)
def setup_table() -> Generator[None, None, None]:
    table.create_table()
    yield
    table.delete_table()


@pytest.fixture(scope="session")
def user_driver() -> UserDriver:
    return UserDriver(table_name=table_name, endpoint_url=endpoint_url)


@pytest.fixture(scope="session")
def user_creation_driver(user_driver: UserDriver) -> UserCreationDriver:
    return UserCreationDriver(user_driver)


@pytest.fixture(scope="session")
def user_desc_driver(user_driver: UserDriver) -> UserDescDriver:
    return UserDescDriver(user_driver)


@pytest.fixture(scope="session")
def user_deletion_driver(user_driver: UserDriver) -> UserDeletionDriver:
    return UserDeletionDriver(user_driver)


@pytest.fixture(scope="session")
def user_update_driver(user_driver: UserDriver) -> UserUpdateDriver:
    return UserUpdateDriver(user_driver)
