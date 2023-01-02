from aws_lambda_typing.events import APIGatewayProxyEventV2
from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from controllers.api import ApiController
from drivers.user_creation import UserCreationDriver
from events.utils import to_api_controller_input
from presenters.ok_simple_response import ok_response_builder
from services.user_creation import UserCreationService
from use_cases.user_creation import UserCreationUseCase
from validators.requests.user_creation import UserCreationRequestValidator

# TODO: fix
use_case = UserCreationUseCase(
    UserCreationService(UserCreationDriver("simple-crud-function"))
)


def handle(event: APIGatewayProxyEventV2) -> APIGatewayProxyResponseV2:
    return (
        ApiController(
            use_case=use_case,
            request_validator=UserCreationRequestValidator,
            ok_response_builder=ok_response_builder,
        )
        .handle(to_api_controller_input(event))
        .serialize()
    )
