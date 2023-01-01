from typing import Literal, TypeVar

from typing_extensions import TypeAlias

CountryCode: TypeAlias = Literal["JPN", "PHL", "USA"]
Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", covariant=True)
