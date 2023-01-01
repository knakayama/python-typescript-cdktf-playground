from typing import Protocol

from modules.type_hints import Input, Output


class UseCaseProtocol(Protocol[Input, Output]):
    def execute(self, input: Input) -> Output:
        ...
