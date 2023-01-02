from entities.user import User
from exceptions.user import UserNotFound
from pydantic import UUID4, BaseModel
from services.user_desc import UserDescServiceProtocol


class UserDescUseCaseInput(BaseModel):
    id: UUID4


class UserDescUseCase:
    def __init__(self, service: UserDescServiceProtocol) -> None:
        self.service = service

    def execute(self, input: UserDescUseCaseInput) -> User:
        user = self.service.describe(input.id)

        if user is None:
            raise UserNotFound(input.id)
        else:
            return user
