from uuid import UUID

import pytest
from pytest import MonkeyPatch
from hypothesis import given
from hypothesis.strategies import uuids

from exceptions.user import UserNotFound
from use_cases.user_desc import UserDescUseCase

from ..fixtures import utils


class TestUserDescUseCase:
    @given(id=uuids(version=4))
    def test_given_non_existing_user(
        self,
        id: UUID,
        user_desc_use_case: UserDescUseCase,
    ) -> None:
        with pytest.raises(UserNotFound):
            user_desc_use_case.execute(id)

    def test_given_an_existing_user(
        self, user_desc_use_case: UserDescUseCase, monkeypatch: MonkeyPatch
    ) -> None:
        user = utils.user()
        monkeypatch.setattr(
            user_desc_use_case.service, "describe", lambda *_args, **_kwargs: user
        )

        assert user_desc_use_case.execute(user.id) == user
