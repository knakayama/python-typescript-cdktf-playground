from uuid import UUID
from hypothesis import given
from hypothesis.strategies import uuids

import pytest
from drivers.user_creation import UserCreationDriver
from drivers.user_deletion import UserDeletionDriver
from drivers.user_desc import UserDescDriver

from ..fixtures import utils


class TestUserDeletionDriver:
    @given(id=uuids(version=4))
    def test_given_non_existing_user(
        self,
        id: UUID,
        user_deletion_driver: UserDeletionDriver,
    ) -> None:
        with pytest.raises(Exception):
            user_deletion_driver.delete(id)

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
