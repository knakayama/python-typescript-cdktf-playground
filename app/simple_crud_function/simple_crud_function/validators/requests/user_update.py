import json

from controllers.protocols import ApiControllerInput
from use_cases.user_update import UserUpdateUseCaseInput


class UserUpdateRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserUpdateUseCaseInput:
        return UserUpdateUseCaseInput(**json.loads(input.body))
