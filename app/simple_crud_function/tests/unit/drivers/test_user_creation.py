from typing import Optional

import pytest
from drivers.user_creation import UserCreationDriver
from drivers.user_desc import UserDescDriver

from tests.unit.fixtures import utils


class TestUserCreationDriver:
    @pytest.mark.parametrize("middle_name", [utils.first_name(), None])
    def test_given_new_users(
        self,
        middle_name: Optional[str],
        user_creation_driver: UserCreationDriver,
        user_desc_driver: UserDescDriver,
    ) -> None:
        user = user_creation_driver.create(utils.user(middle_name))

        assert user_desc_driver.describe(user.id) == user

    def test_given_an_existing_user(
        self, user_creation_driver: UserCreationDriver
    ) -> None:
        user = user_creation_driver.create(utils.user())

        with pytest.raises(Exception):
            user_creation_driver.create(user)
