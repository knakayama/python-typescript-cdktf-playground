from entities.user import User
from services.user_protocols import UserCreationServiceProtocol


class UserCreationUseCase:
    def __init__(self, service: UserCreationServiceProtocol) -> None:
        self.service = service

    def execute(self, input: User) -> User:
        return self.service.create(input)
