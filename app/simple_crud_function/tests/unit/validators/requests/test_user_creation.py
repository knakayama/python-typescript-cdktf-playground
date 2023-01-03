import json

import pytest
from controllers.protocols import ApiControllerInput
from hypothesis import given
from hypothesis import strategies as st
from modules.type_hints import CountryCode
from pydantic import EmailStr, ValidationError
from validators.requests.user_creation import UserCreationRequestValidator


class TestUserCreationRequestValidator:
    @given(
        first_name=st.text(min_size=1, max_size=20),
        middle_name=st.one_of(st.text(min_size=1, max_size=20), st.none()),
        last_name=st.text(min_size=1, max_size=20),
        age=st.integers(min_value=0, max_value=150),
        address=st.text(min_size=1, max_size=200),
        zip_code=st.text(min_size=1, max_size=50),
        # TODO: type error
        country=st.from_type(CountryCode),  # type: ignore
        email=st.from_type(EmailStr),
    )
    def test_given_expected_input(
        self,
        path_parameters: dict[str, str],
        **kwargs: object,
    ) -> None:
        UserCreationRequestValidator().parse(
            ApiControllerInput(
                path_parameters=path_parameters,
                body=json.dumps(kwargs),
            )
        ).dict() == kwargs

    @given(
        first_name=st.text(min_size=21),  # invalid
        middle_name=st.one_of(st.text(min_size=1, max_size=20), st.none()),
        last_name=st.text(min_size=1, max_size=20),
        age=st.integers(min_value=0, max_value=150),
        address=st.text(min_size=1, max_size=200),
        zip_code=st.text(min_size=1, max_size=50),
        country=st.from_type(CountryCode),  # type: ignore
        email=st.from_type(EmailStr),
    )
    def test_given_invalid_input(
        self,
        path_parameters: dict[str, str],
        **kwargs: object,
    ) -> None:
        with pytest.raises(ValidationError):
            UserCreationRequestValidator().parse(
                ApiControllerInput(
                    path_parameters=path_parameters,
                    body=json.dumps(kwargs),
                )
            )
