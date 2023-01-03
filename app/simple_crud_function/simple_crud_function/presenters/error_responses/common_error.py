from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from presenters.error_responses.response_builder import (
    ErrorResponseBody,
    ErrorResponseBuilder,
)


class CommonErrorResponseBuilder:
    def __init__(self, error: Exception, status_code: int) -> None:
        self.response_builder = ErrorResponseBuilder(
            response_body=ErrorResponseBody(
                code=error.__class__.__name__,
                desc=f"{error}",
            ),
            status_code=status_code,
        )

    def serialize(self) -> APIGatewayProxyResponseV2:
        return self.response_builder.serialize()
