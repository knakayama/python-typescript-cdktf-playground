from typing import Callable, Protocol

from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from modules.type_hints import CovariantType
from typing_extensions import TypeAlias


class ResponseBuilderProtocol(Protocol):
    def serialize(self) -> APIGatewayProxyResponseV2:
        ...


OKResponseBuilderFactory: TypeAlias = Callable[[CovariantType], ResponseBuilderProtocol]
