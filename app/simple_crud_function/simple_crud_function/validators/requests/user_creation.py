import json

from controllers.protocols import ApiControllerInput
from use_cases.user_creation import UserCreationUseCaseInput


class UserCreationRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserCreationUseCaseInput:
        return UserCreationUseCaseInput(**json.loads(input.body))
