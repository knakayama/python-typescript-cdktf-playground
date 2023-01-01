from typing import Protocol, TypeVar

Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", covariant=True)


class ApiControllerProtocol(Protocol[Input, Output]):
    def handle(self, input: Input) -> Output:
        ...
