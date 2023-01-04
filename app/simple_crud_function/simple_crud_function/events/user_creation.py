from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_typing.events import APIGatewayProxyEventV2
from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from controllers.api import ApiController
from drivers.user import UserDriver
from drivers.user_creation import UserCreationDriver
from events.utils import to_api_controller_input
from presenters.ok_responses.common import ok_response_builder
from services.user_creation import UserCreationService
from use_cases.user_creation import UserCreationUseCase
from validators.requests.user_creation import UserCreationRequestValidator

use_case = UserCreationUseCase(UserCreationService(UserCreationDriver(UserDriver())))


def handle(
    event: APIGatewayProxyEventV2, _context: LambdaContext
) -> APIGatewayProxyResponseV2:
    return (
        ApiController(
            use_case=use_case,
            request_validator=UserCreationRequestValidator,
            ok_response_builder=ok_response_builder,
        )
        .handle(to_api_controller_input(event))
        .serialize()
    )
