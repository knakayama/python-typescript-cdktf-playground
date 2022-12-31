from typing import Generator

import pytest
from drivers.user_creation import UserCreationDriver
from drivers.user_deletion import UserDeletionDriver
from drivers.user_desc import UserDescDriver
from modules.constants import endpoint_url, table_name

from ..fixtures.table import TableFixture

table = TableFixture(table_name=table_name, endpoint_url=endpoint_url)


@pytest.fixture(scope="session", autouse=True)
def setup_table() -> Generator[None, None, None]:
    table.create_table()
    yield
    table.delete_table()


@pytest.fixture(scope="session")
def user_creation_driver() -> UserCreationDriver:
    return UserCreationDriver(table_name=table_name, endpoint_url=endpoint_url)


@pytest.fixture(scope="session")
def user_desc_driver() -> UserDescDriver:
    return UserDescDriver(table_name=table_name, endpoint_url=endpoint_url)


@pytest.fixture(scope="session")
def user_deletion_driver() -> UserDeletionDriver:
    return UserDeletionDriver(table_name=table_name, endpoint_url=endpoint_url)
