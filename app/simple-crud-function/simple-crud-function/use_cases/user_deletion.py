from uuid import UUID

from services.user_deletion import UserDeletionServiceProtocol


class UserDeletionUseCase:
    def __init__(self, service: UserDeletionServiceProtocol) -> None:
        self.service = service

    def execute(self, input: UUID) -> None:
        self.service.delete(input)
