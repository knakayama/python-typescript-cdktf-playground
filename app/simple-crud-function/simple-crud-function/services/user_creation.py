from drivers.user_protocols import UserCreationDriverProtocol
from entities.user import User


class UserCreationService:
    def __init__(self, driver: UserCreationDriverProtocol) -> None:
        self.driver = driver

    def create(self, user: User) -> User:
        return self.driver.create(user)
