from typing import Callable, Protocol

from controllers.protocols import ApiControllerInput
from modules.type_hints import CovariantType
from typing_extensions import TypeAlias


class RequestValidatorProtocol(Protocol[CovariantType]):
    def parse(self, input: ApiControllerInput) -> CovariantType:
        ...


RequestValidatorFactory: TypeAlias = Callable[
    [], RequestValidatorProtocol[CovariantType]
]
