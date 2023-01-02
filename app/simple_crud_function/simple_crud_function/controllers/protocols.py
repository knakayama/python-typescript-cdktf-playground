from dataclasses import dataclass
from typing import Protocol

from presenters.protocols import ResponseBuilderProtocol


@dataclass
class ApiControllerInput:
    path_parameters: dict[str, str]
    body: str


class ControllerProtocol(Protocol):
    def handle(self, input: ApiControllerInput) -> ResponseBuilderProtocol:
        ...
