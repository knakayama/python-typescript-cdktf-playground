from controllers.protocols import ApiControllerInput
from use_cases.user_deletion import UserDeletionAndUpdateUseCaseInput


class UserDeletionAndUpdateRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserDeletionAndUpdateUseCaseInput:
        return UserDeletionAndUpdateUseCaseInput(**input.path_parameters)
