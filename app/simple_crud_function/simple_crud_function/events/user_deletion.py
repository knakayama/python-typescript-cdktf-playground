from aws_lambda_typing.events import APIGatewayProxyEventV2
from aws_lambda_typing.responses import APIGatewayProxyResponseV2
from controllers.api import ApiController
from drivers.user import UserDriver
from drivers.user_deletion import UserDeletionDriver
from events.utils import to_api_controller_input
from presenters.ok_responses.no_content import ok_response_builder
from services.user_deletion import UserDeletionService
from use_cases.user_deletion import UserDeletionUseCase
from validators.requests.user_deletion_and_desc import (
    UserDeletionAndUpdateRequestValidator,
)

use_case = UserDeletionUseCase(UserDeletionService(UserDeletionDriver(UserDriver())))


def handle(event: APIGatewayProxyEventV2) -> APIGatewayProxyResponseV2:
    return (
        ApiController(
            use_case=use_case,
            request_validator=UserDeletionAndUpdateRequestValidator,
            ok_response_builder=ok_response_builder,
        )
        .handle(to_api_controller_input(event))
        .serialize()
    )
