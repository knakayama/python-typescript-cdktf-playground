from typing import Optional


def to_name(first_name: str, middle_name: Optional[str], last_name: str) -> str:
    middle_name = " " if middle_name is None else f", {middle_name}, "
    return f"{first_name}{middle_name}{last_name}"
