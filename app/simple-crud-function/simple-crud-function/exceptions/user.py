class UserNotFound(Exception):
    def __init__(self, id: str) -> None:
        self.message = f"User {id} not found"
        super().__init__(self.message)
