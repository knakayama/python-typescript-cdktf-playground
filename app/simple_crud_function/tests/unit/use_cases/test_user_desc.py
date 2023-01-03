from uuid import UUID

import pytest
from exceptions.user import UserNotFound
from hypothesis import given
from hypothesis.strategies import uuids
from pytest import MonkeyPatch
from use_cases.user_deletion import UserDeletionAndUpdateUseCaseInput
from use_cases.user_desc import UserDescUseCase

from tests.unit.fixtures import utils


class TestUserDescUseCase:
    @given(id=uuids(version=4))
    def test_given_non_existing_user(
        self,
        id: UUID,
        user_desc_use_case: UserDescUseCase,
    ) -> None:
        with pytest.raises(UserNotFound):
            user_desc_use_case.execute(UserDeletionAndUpdateUseCaseInput(user_id=id))

    def test_given_an_existing_user(
        self, user_desc_use_case: UserDescUseCase, monkeypatch: MonkeyPatch
    ) -> None:
        user = utils.user()
        monkeypatch.setattr(
            user_desc_use_case.user_desc_service,
            "describe",
            lambda *_args, **_kwargs: user,
        )

        assert (
            user_desc_use_case.execute(
                UserDeletionAndUpdateUseCaseInput(user_id=user.id)
            )
            == user
        )
