from typing import Any

from presenters.error_response import ErrorResponseBody


def to_error_response_body_dict(error: Exception) -> dict[str, Any]:
    return ErrorResponseBody(code=error.__class__.__name__, desc=f"{error}").__dict__
