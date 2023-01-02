from presenters.error_responses import (
    InternalServerErrorResponseBuilder,
    NotFoundResponseBuilder,
)
from presenters.protocols import ResponseBuilderProtocol
from exceptions.user import UserNotFound


def error_response_builder(error: Exception) -> ResponseBuilderProtocol:
    if isinstance(error, UserNotFound):
        return NotFoundResponseBuilder(error)
    else:
        return InternalServerErrorResponseBuilder(error)
