from typing import Generic

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from modules.type_hints import VariantType
from presenters.ok_responses.response_builder import OKResponseBuilder
from presenters.protocols import ResponseBuilderProtocol


class CommonResponseBuilder(Generic[VariantType]):
    def __init__(self, input: VariantType) -> None:
        self.response_builder = OKResponseBuilder(input)

    def serialize(self) -> APIGatewayProxyResponseV2:
        return self.response_builder.serialize()


def ok_response_builder(input: VariantType) -> ResponseBuilderProtocol:
    return CommonResponseBuilder(input)
