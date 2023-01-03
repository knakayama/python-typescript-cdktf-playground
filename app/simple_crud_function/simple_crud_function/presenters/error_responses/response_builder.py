import json
from dataclasses import dataclass

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from exceptions.user import UserNotFound
from presenters.error_responses.common_error import CommonErrorResponseBuilder
from presenters.error_responses.internal_server_error import (
    InternalServerErrorResponseBuilder,
)
from presenters.http_status_code import HttpStatusCode
from presenters.protocols import ResponseBuilderProtocol
from pydantic import ValidationError


@dataclass
class ErrorResponseBody:
    code: str
    desc: str


class ErrorResponseBuilder:
    def __init__(self, response_body: ErrorResponseBody, status_code: int) -> None:
        self.response_body = response_body
        self.status_code = status_code

    def serialize(self) -> APIGatewayProxyResponseV2:
        return APIGatewayProxyResponseV2(
            statusCode=self.status_code, body=json.dumps(self.response_body.__dict__)
        )


def error_response_builder(error: Exception) -> ResponseBuilderProtocol:
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
