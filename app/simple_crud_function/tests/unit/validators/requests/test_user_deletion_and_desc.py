from typing import Any

import pytest
from controllers.protocols import ApiControllerInput
from hypothesis import given
from hypothesis import strategies as st
from pydantic import ValidationError
from validators.requests.user_deletion_and_desc import (
    UserDeletionAndDescRequestValidator,
)


class TestUserDeletionAndDescRequestValidator:
    @given(path_parameters=st.fixed_dictionaries({"user_id": st.uuids(version=4)}))
    def test_given_expected_input(
        self, path_parameters: dict[str, str], body: str
    ) -> None:
        UserDeletionAndDescRequestValidator().parse(
            ApiControllerInput(
                path_parameters=path_parameters,
                body=body,
            )
        ).dict() == path_parameters

    @given(path_parameters=st.fixed_dictionaries({"user_id": st.randoms()}))
    def test_given_invalid_input(
        self, path_parameters: dict[str, Any], body: str
    ) -> None:
        with pytest.raises(ValidationError):
            UserDeletionAndDescRequestValidator().parse(
                ApiControllerInput(
                    path_parameters=path_parameters,
                    body=body,
                )
            )
