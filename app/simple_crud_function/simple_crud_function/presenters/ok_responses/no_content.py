from dataclasses import dataclass
from typing import Generic, Optional

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from modules.type_hints import VariantType
from presenters.http_status_code import HttpStatusCode
from presenters.ok_responses.response_builder import OKResponseBuilder
from presenters.protocols import ResponseBuilderProtocol


@dataclass
class NoContent:
    pass


class NoContentResponseBuilder(Generic[VariantType]):
    def __init__(self, input: VariantType) -> None:
        self.response_builder = OKResponseBuilder(
            http_status_code=HttpStatusCode.NoContent, response_body=input
        )

    def serialize(self) -> APIGatewayProxyResponseV2:
        return self.response_builder.serialize()


def ok_response_builder(
    _input: Optional[VariantType] = None,
) -> ResponseBuilderProtocol:
    return NoContentResponseBuilder(NoContent())
