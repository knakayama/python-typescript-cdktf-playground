from pydantic import UUID4, BaseModel
from services.user_deletion import UserDeletionServiceProtocol


class UserDeletionUseCaseInput(BaseModel):
    id: UUID4


class UserDeletionUseCase:
    def __init__(self, service: UserDeletionServiceProtocol) -> None:
        self.service = service

    def execute(self, input: UserDeletionUseCaseInput) -> None:
        # TODO: implement user not found
        self.service.delete(input.id)
