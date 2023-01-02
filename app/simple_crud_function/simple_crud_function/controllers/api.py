from typing import Generic

from controllers.protocols import ApiControllerInput
from modules.type_hints import ContravariantType, CovariantType
from presenters.error_response import error_response_builder
from presenters.protocols import OKResponseBuilderFactory, ResponseBuilderProtocol
from use_cases.protocols import UseCaseProtocol
from validators.requests.protocols import RequestValidatorFactory
from validators.requests.utils import make_request_validator


class ApiController(Generic[ContravariantType, CovariantType]):
    def __init__(
        self,
        use_case: UseCaseProtocol[ContravariantType, CovariantType],
        request_validator: RequestValidatorFactory[ContravariantType],
        ok_response_builder: OKResponseBuilderFactory[CovariantType],
    ) -> None:
        self.use_case = use_case
        self.request_validator = request_validator
        self.ok_response_builder = ok_response_builder

    def handle(self, input: ApiControllerInput) -> ResponseBuilderProtocol:
        print(input)

        try:
            request_validator = make_request_validator(self.request_validator)
            request = request_validator.parse(input)

            output = self.use_case.execute(request)
            return self.ok_response_builder(output)
        except Exception as error:
            return error_response_builder(error)
