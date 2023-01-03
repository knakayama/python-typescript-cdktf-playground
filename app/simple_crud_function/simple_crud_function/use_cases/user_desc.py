from entities.user import User
from exceptions.user import UserNotFound
from pydantic import UUID4, BaseModel
from services.user_desc import UserDescServiceProtocol


class UserDescUseCaseInput(BaseModel):
    id: UUID4


class UserDescUseCase:
    def __init__(self, user_desc_service: UserDescServiceProtocol) -> None:
        self.user_desc_service = user_desc_service

    def execute(self, input: UserDescUseCaseInput) -> User:
        user = self.user_desc_service.describe(input.id)

        if user is None:
            raise UserNotFound(input.id)
        else:
            return user
