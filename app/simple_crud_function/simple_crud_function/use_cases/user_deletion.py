from pydantic import UUID4, BaseModel
from services.user_deletion import UserDeletionServiceProtocol


class UserDeletionAndUpdateUseCaseInput(BaseModel):
    user_id: UUID4


class UserDeletionUseCase:
    def __init__(self, user_deletion_service: UserDeletionServiceProtocol) -> None:
        self.user_deletion_service = user_deletion_service

    def execute(self, input: UserDeletionAndUpdateUseCaseInput) -> None:
        self.user_deletion_service.delete(input.user_id)
