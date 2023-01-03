from controllers.protocols import ApiControllerInput
from use_cases.user_desc import UserDescUseCaseInput


class UserDescRequestValidator:
    def parse(self, input: ApiControllerInput) -> UserDescUseCaseInput:
        return UserDescUseCaseInput(**input.path_parameters)
