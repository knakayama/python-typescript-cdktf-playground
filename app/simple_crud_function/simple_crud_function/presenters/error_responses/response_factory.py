from exceptions.user import UserNotFound
from presenters.error_responses.common_error import CommonErrorResponseBuilder
from presenters.error_responses.internal_server_error import (
    InternalServerErrorResponseBuilder,
)
from presenters.http_status_code import HttpStatusCode
from presenters.protocols import ResponseBuilderProtocol
from pydantic import ValidationError


def make_error_response_builder(error: Exception) -> ResponseBuilderProtocol:
    if isinstance(error, ValidationError):
        return CommonErrorResponseBuilder(
            error=error, status_code=HttpStatusCode.BadRequest
        )
    elif isinstance(error, UserNotFound):
        return CommonErrorResponseBuilder(
            error=error, status_code=HttpStatusCode.NotFound
        )
    else:
        return InternalServerErrorResponseBuilder(error)
