from uuid import UUID
from entities.user import User
from services.user_protocols import UserDescServiceProtocol
from exceptions.user import UserNotFound


class UserDescUseCase:
    def __init__(self, service: UserDescServiceProtocol) -> None:
        self.service = service

    def execute(self, id: UUID) -> User:
        user = self.service.describe(id)

        if user is None:
            raise UserNotFound(id)
        else:
            return user
