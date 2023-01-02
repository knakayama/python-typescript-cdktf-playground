from uuid import UUID


class UserNotFound(Exception):
    def __init__(self, id: UUID) -> None:
        self.message = f"User {id} not found"
        super().__init__(self.message)
