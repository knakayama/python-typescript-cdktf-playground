from typing import Generic

from modules.type_hints import Input, Output
from use_cases.protocols import UseCaseProtocol


class ApiController(Generic[Input, Output]):
    def __init__(self, use_case: UseCaseProtocol[Input, Output]) -> None:
        self.use_case = use_case

    def handle(self, input: Input) -> Output:
        return self.use_case.execute(input)
