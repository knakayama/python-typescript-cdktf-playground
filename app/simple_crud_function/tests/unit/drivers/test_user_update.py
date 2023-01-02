from typing import Optional

import pytest
from drivers.user_creation import UserCreationDriver
from drivers.user_desc import UserDescDriver
from drivers.user_update import UserUpdateDriver

from tests.unit.fixtures import utils


class TestUserUpdateDriver:
    @pytest.mark.parametrize("middle_name", [utils.first_name(), None])
    def test_given_new_users(
        self,
        middle_name: Optional[str],
        user_update_driver: UserUpdateDriver,
        user_creation_driver: UserCreationDriver,
        user_desc_driver: UserDescDriver,
    ) -> None:
        updated_user = user_update_driver.update(
            user_creation_driver.create(utils.user(middle_name))
        )

        assert user_desc_driver.describe(updated_user.id) == updated_user

    def test_given_non_existing_user(
        self, user_update_driver: UserUpdateDriver
    ) -> None:
        with pytest.raises(Exception):
            user_update_driver.update(utils.user())
