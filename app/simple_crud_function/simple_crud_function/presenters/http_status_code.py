from typing import ClassVar


class HttpStatusCode:
    OK: ClassVar[int] = 200
    BadRequest: ClassVar[int] = 400
    NotFound: ClassVar[int] = 404
    InternalServerError: ClassVar[int] = 500
