from typing import Protocol, TypeVar

Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", covariant=True)


class UseCaseProtocol(Protocol[Input, Output]):
    def execute(self, input: Input) -> Output:
        ...
