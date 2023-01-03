from typing import Any, Generator, TypedDict

import pytest
from botocore.exceptions import ClientError
from drivers.user import UserDriver
from drivers.user_creation import UserCreationDriver
from drivers.user_deletion import UserDeletionDriver
from drivers.user_desc import UserDescDriver
from drivers.user_update import UserUpdateDriver

from tests.unit.constants import endpoint_url, table_name
from tests.unit.fixtures import utils
from tests.unit.fixtures.table import TableFixture

table = TableFixture(table_name=table_name, endpoint_url=endpoint_url)


class _CustomResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, Any]
    RetryAttempts: int


class _CustomClientErrorResponseError(TypedDict, total=False):
    Code: str
    Message: str


class _CustomClientErrorResponseTypeDef(TypedDict, total=False):
    Status: str
    StatusReason: str
    Error: _CustomClientErrorResponseError
    ResponseMetadata: _CustomResponseMetadataTypeDef


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


@pytest.fixture(scope="function")
def client_error() -> ClientError:
    return ClientError(
        operation_name=utils.string(),
        error_response=_CustomClientErrorResponseTypeDef(
            Status=utils.string(),
            StatusReason=utils.string(),
            Error=_CustomClientErrorResponseError(
                Code=utils.string(),
                Message=utils.string(),
            ),
            ResponseMetadata=_CustomResponseMetadataTypeDef(
                RequestId=utils.string(),
                HostId=utils.string(),
                HTTPStatusCode=utils.number(),
                HTTPHeaders=utils.dictionary(),
                RetryAttempts=utils.number(),
            ),
        ),
    )
