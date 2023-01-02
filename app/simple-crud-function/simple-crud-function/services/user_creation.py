from typing import Protocol
from drivers.user_creation import UserCreationDriverProtocol
from entities.user import User
from typing_extensions import TypeAlias
from use_cases.user_creation import UserCreationUseCaseInput

UserCreationServiceInput: TypeAlias = UserCreationUseCaseInput
UserCreationServiceOutput: TypeAlias = User


class UserCreationServiceProtocol(Protocol):
    def create(self, input: UserCreationServiceInput) -> UserCreationServiceOutput:
        ...


class UserCreationService:
    def __init__(self, driver: UserCreationDriverProtocol) -> None:
        self.driver = driver

    def create(self, input: UserCreationServiceInput) -> UserCreationServiceOutput:
        return self.driver.create(User(**input.dict()))
