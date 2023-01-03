import json
from dataclasses import dataclass

from aws_lambda_typing.responses import APIGatewayProxyResponseV2


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
