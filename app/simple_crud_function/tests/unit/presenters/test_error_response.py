import json

import pytest
from exceptions.user import UserNotFound
from presenters.error_responses.response_factory import make_error_response_builder
from presenters.http_status_code import HttpStatusCode
from pydantic import BaseModel, ValidationError

from tests.unit.fixtures import utils
from tests.unit.presenters.utils import to_error_response_body_dict


class TestErrorResponseBuilder:
    @pytest.mark.parametrize("error", [UserNotFound(id=utils.user_id())])
    def test_given_not_found_matchables(self, error: Exception) -> None:
        output = make_error_response_builder(error).serialize()

        assert output["statusCode"] == HttpStatusCode.NotFound
        assert json.loads(output["body"]) == to_error_response_body_dict(error)

    @pytest.mark.parametrize(
        "error",
        [
            ValidationError(
                errors=[],
                model=BaseModel,
            )
        ],
    )
    def test_given_bad_request_matchables(self, error: Exception) -> None:
        output = make_error_response_builder(error).serialize()

        assert output["statusCode"] == HttpStatusCode.BadRequest
        assert json.loads(output["body"]) == to_error_response_body_dict(error)

    @pytest.mark.parametrize("error", [Exception(utils.string())])
    def test_given_no_matchables(sel, error: Exception) -> None:
        output = make_error_response_builder(error).serialize()

        assert output["statusCode"] == HttpStatusCode.InternalServerError
        assert json.loads(output["body"]) == {
            "code": "InternalServerError",
            "desc": "Something wrong occurred.",
        }
