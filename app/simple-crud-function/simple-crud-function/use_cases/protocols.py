from typing import Protocol

from modules.type_hints import ContravariantType, CovariantType


class UseCaseProtocol(Protocol[ContravariantType, CovariantType]):
    def execute(self, input: ContravariantType) -> CovariantType:
        ...
