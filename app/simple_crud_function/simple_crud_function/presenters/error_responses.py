import json
from dataclasses import dataclass

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from presenters.http_status_code import HttpStatusCode


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


class NotFoundResponseBuilder:
    def __init__(self, error: Exception) -> None:
        self.response_builder = ErrorResponseBuilder(
            response_body=ErrorResponseBody(
                code=error.__class__.__name__,
                desc=f"{error}",
            ),
            status_code=HttpStatusCode.NotFound,
        )

    def serialize(self) -> APIGatewayProxyResponseV2:
        return self.response_builder.serialize()


class InternalServerErrorResponseBuilder:
    def __init__(self, error: Exception) -> None:
        print(error)

        self.response_builder = ErrorResponseBuilder(
            response_body=ErrorResponseBody(
                code="InternalServerError", desc="Something wrong occurred."
            ),
            status_code=HttpStatusCode.InternalServerError,
        )

    def serialize(self) -> APIGatewayProxyResponseV2:
        return self.response_builder.serialize()
