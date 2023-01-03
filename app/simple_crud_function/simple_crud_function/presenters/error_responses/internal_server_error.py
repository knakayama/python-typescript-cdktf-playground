from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from presenters.error_responses.response_builder import (
    ErrorResponseBody,
    ErrorResponseBuilder,
)
from presenters.http_status_code import HttpStatusCode


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
