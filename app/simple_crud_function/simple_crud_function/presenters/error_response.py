from presenters.error_responses import InternalServerErrorResponseBuilder
from presenters.protocols import ResponseBuilderProtocol


def error_response_builder(error: Exception) -> ResponseBuilderProtocol:
    # TODO: implement
    return InternalServerErrorResponseBuilder(error)
