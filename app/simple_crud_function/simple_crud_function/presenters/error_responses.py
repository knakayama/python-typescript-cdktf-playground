import json
from dataclasses import dataclass

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from presenters.http_status_code import HttpStatusCode


@dataclass
class ErrorResponseBody:
    code: str
    desc: str


class ErrorResponseBuilder:
    def __init__(
        self, error_response_body: ErrorResponseBody, http_status_code: int
    ) -> None:
        self.error_response_body = error_response_body
        self.http_status_code = http_status_code

    def serialize(self) -> APIGatewayProxyResponseV2:
        return APIGatewayProxyResponseV2(
            statusCode=self.http_status_code, body=json.dumps(self.error_response_body)
        )


class InternalServerErrorResponseBuilder:
    def __init__(self, error: Exception) -> None:
        print(error)

        self.response_builder = ErrorResponseBuilder(
            error_response_body=ErrorResponseBody(
                code="Internal Server Error", desc="Something wrong occurred."
            ),
            http_status_code=HttpStatusCode.InternalServerError,
        )

    def serialize(self) -> APIGatewayProxyResponseV2:
        return self.response_builder.serialize()
