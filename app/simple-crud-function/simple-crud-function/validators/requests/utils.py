from modules.type_hints import VariantType
from validators.requests.protocols import (
    RequestValidatorFactory,
    RequestValidatorProtocol,
)


def make_request_validator(
    request_validator: RequestValidatorFactory[VariantType],
) -> RequestValidatorProtocol[VariantType]:
    return request_validator()
