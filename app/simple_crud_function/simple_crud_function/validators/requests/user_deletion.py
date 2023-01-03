from controllers.protocols import ApiControllerInput
from use_cases.user_deletion import UserDeletionUseCaseInput


class UserDeletionRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserDeletionUseCaseInput:
        return UserDeletionUseCaseInput(**input.path_parameters)
