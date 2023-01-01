from typing import Protocol

from modules.type_hints import Input, Output


class ControllerProtocol(Protocol[Input, Output]):
    def handle(self, input: Input) -> Output:
        ...
