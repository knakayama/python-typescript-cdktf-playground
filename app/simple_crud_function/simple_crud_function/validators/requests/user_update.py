import json

from controllers.protocols import ApiControllerInput
from use_cases.user_update import UserUpdateUseCaseInput


class UserUpdateRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserUpdateUseCaseInput:
        return UserUpdateUseCaseInput(
            **dict(
                {"id": input.path_parameters["user_id"]},
                **json.loads(input.body),
            )
        )
