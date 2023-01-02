from typing import Literal, TypeVar

from typing_extensions import TypeAlias

CountryCode: TypeAlias = Literal["JPN", "PHL", "USA"]
VariantType = TypeVar("VariantType")
CovariantType = TypeVar("CovariantType", covariant=True)
ContravariantType = TypeVar("ContravariantType", contravariant=True)
