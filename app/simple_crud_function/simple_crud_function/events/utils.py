from aws_lambda_typing.events import APIGatewayProxyEventV2
from controllers.protocols import ApiControllerInput


def to_api_controller_input(event: APIGatewayProxyEventV2) -> ApiControllerInput:
    return ApiControllerInput(
        path_parameters=event.get("pathParameters", {}),
        body=event.get("body", ""),
    )
