from typing import Protocol


# TODO: Python doesn't support generic interface?
# https://stackoverflow.com/questions/61467673/how-do-i-create-a-generic-interface-in-python
class UseCaseProtocol(Protocol):
    def execute(self, user: object) -> object:
        ...
