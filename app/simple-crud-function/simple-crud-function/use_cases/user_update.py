from entities.user import User
from services.user_protocols import UserUpdateServiceProtocol


class UserUpdateUseCase:
    def __init__(self, service: UserUpdateServiceProtocol) -> None:
        self.service = service

    def execute(self, input: User) -> User:
        return self.service.update(input)
