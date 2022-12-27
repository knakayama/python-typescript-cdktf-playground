from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_typing.events import APIGatewayProxyEventV2


def handle(
    event: APIGatewayProxyEventV2, context: LambdaContext
) -> APIGatewayProxyEventV2:
    return event
