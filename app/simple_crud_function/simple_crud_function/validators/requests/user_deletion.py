import json

from controllers.protocols import ApiControllerInput
from use_cases.user_deletion import UserDeletionUseCaseInput


class UserDeletionRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserDeletionUseCaseInput:
        return UserDeletionUseCaseInput(**json.loads(input.body))
