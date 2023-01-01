from typing import TypeVar

from use_cases.protocols import UseCaseProtocol

Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", covariant=True)


class ApiController:
    def __init__(self, use_case: UseCaseProtocol[Input, Output]) -> None:
        self.use_case = use_case

    # TODO: fix
    # A function returning TypeVar should receive at least one argument
    # containing the same TypeVar  [type-var]
    def handle(self, input: Input) -> Output:  # type: ignore
        return self.use_case.execute(input)
