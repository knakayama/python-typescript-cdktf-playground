from drivers.user_protocol import UserUpdateDriverProtocol
from entities.user import User


class UserUpdateService:
    def __init__(self, driver: UserUpdateDriverProtocol) -> None:
        self.driver = driver

    def update(self, user: User) -> User:
        return self.driver.update(user)
