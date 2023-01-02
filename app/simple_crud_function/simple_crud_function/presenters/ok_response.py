import json
from typing import Generic

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from modules.type_hints import CovariantType
from presenters.http_status_code import HttpStatusCode


class OKResponseBuilder(Generic[CovariantType]):
    def __init__(
        self, response_body: CovariantType, http_status_code: int = HttpStatusCode.OK
    ) -> None:
        self.response_body = response_body
        self.status_code = http_status_code

    def serialize(self) -> APIGatewayProxyResponseV2:
        return APIGatewayProxyResponseV2(
            statusCode=self.status_code, body=json.dumps(self.response_body)
        )
