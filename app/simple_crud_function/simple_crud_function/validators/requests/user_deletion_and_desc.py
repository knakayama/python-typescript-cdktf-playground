from controllers.protocols import ApiControllerInput
from use_cases.user_deletion import UserDeletionAndUpdateUseCaseInput


class UserDeletionAndDescRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserDeletionAndUpdateUseCaseInput:
        return UserDeletionAndUpdateUseCaseInput(**input.path_parameters)
