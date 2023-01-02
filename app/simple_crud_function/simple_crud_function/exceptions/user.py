from uuid import UUID


class UserNotFound(Exception):
    def __init__(self, id: UUID) -> None:
        super().__init__(f"User {id} not found")
