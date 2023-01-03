from entities.user import User
from exceptions.user import UserNotFound
from services.user_desc import UserDescServiceProtocol
from use_cases.user_deletion import UserDeletionAndUpdateUseCaseInput


class UserDescUseCase:
    def __init__(self, user_desc_service: UserDescServiceProtocol) -> None:
        self.user_desc_service = user_desc_service

    def execute(self, input: UserDeletionAndUpdateUseCaseInput) -> User:
        user = self.user_desc_service.describe(input.user_id)

        if user is None:
            raise UserNotFound(input.user_id)
        else:
            return user
