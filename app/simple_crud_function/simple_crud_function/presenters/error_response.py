from exceptions.user import UserNotFound
from presenters.error_responses import (
    InternalServerErrorResponseBuilder,
    NotFoundResponseBuilder,
)
from presenters.protocols import ResponseBuilderProtocol


def error_response_builder(error: Exception) -> ResponseBuilderProtocol:
    if isinstance(error, UserNotFound):
        return NotFoundResponseBuilder(error)
    else:
        return InternalServerErrorResponseBuilder(error)
