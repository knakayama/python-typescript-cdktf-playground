from uuid import UUID

import pytest
from drivers.user_creation import UserCreationDriver
from drivers.user_desc import UserDescDriver
from hypothesis import given
from hypothesis.strategies import uuids

from ..fixtures import utils


class TestUserDescDriver:
    @given(id=uuids(version=4))
    def test_given_non_existing_user_id(
        self, id: UUID, user_desc_driver: UserDescDriver
    ) -> None:
        assert user_desc_driver.describe(id) is None

    @pytest.mark.parametrize("middle_name", [utils.first_name(), None])
    def test_given_existing_user_id(
        self,
        middle_name: str,
        user_desc_driver: UserDescDriver,
        user_creation_driver: UserCreationDriver,
    ) -> None:
        user = user_creation_driver.create(utils.user(middle_name))

        assert user_desc_driver.describe(user.id) == user
