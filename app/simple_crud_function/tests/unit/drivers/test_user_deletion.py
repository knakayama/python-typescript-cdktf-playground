from uuid import UUID

import pytest
from botocore.exceptions import ClientError
from drivers.user import UserDriver
from drivers.user_creation import UserCreationDriver
from drivers.user_deletion import UserDeletionDriver
from drivers.user_desc import UserDescDriver
from exceptions.user import UserNotFound
from hypothesis import given
from hypothesis.strategies import uuids
from pytest import MonkeyPatch

from tests.unit.fixtures import utils


class TestUserDeletionDriver:
    @given(id=uuids(version=4))
    def test_given_non_existing_user(
        self,
        id: UUID,
        user_deletion_driver: UserDeletionDriver,
    ) -> None:
        with pytest.raises(UserNotFound):
            user_deletion_driver.delete(id)

    def test_unknown_client_error_occurs(
        self,
        user_driver: UserDriver,
        monkeypatch: MonkeyPatch,
    ) -> None:
        def client_error(*_args: object, **_kwargs: object) -> None:
            raise ClientError  # type: ignore

        monkeypatch.setattr(user_driver.table, "delete_item", client_error)

        driver = UserDeletionDriver(user_driver)

        with pytest.raises(Exception):
            driver.delete(utils.user_id())

    def test_unknown_error_occurs(
        self,
        user_driver: UserDriver,
        monkeypatch: MonkeyPatch,
    ) -> None:
        def error(*_args: object, **_kwargs: object) -> None:
            raise Exception

        monkeypatch.setattr(user_driver.table, "delete_item", error)

        driver = UserDeletionDriver(user_driver)

        with pytest.raises(Exception):
            driver.delete(utils.user_id())

    @pytest.mark.parametrize("middle_name", [utils.first_name(), None])
    def test_given_an_existing_user(
        self,
        middle_name: str,
        user_deletion_driver: UserDeletionDriver,
        user_creation_driver: UserCreationDriver,
        user_desc_driver: UserDescDriver,
    ) -> None:
        user = user_creation_driver.create(utils.user(middle_name))
        user_deletion_driver.delete(user.id)

        assert user_desc_driver.describe(user.id) is None
