import json

from controllers.protocols import ApiControllerInput
from use_cases.user_creation import UserCreationUseCaseInput


# TODO: I think I don't have to make classes for every use case
class UserCreationRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserCreationUseCaseInput:
        return UserCreationUseCaseInput(**json.loads(input.body))
