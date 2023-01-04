from aws_lambda_typing.events import APIGatewayProxyEventV2
from controllers.protocols import ApiControllerInput
from events.utils import to_api_controller_input
from hypothesis import given
from hypothesis import strategies as st


class TestToApiControllerInput:
    @given(
        event=st.dictionaries(
            keys=st.text(),
            values=st.randoms(),
        )
    )
    def test_given_unexpected_event(self, event: APIGatewayProxyEventV2) -> None:
        assert to_api_controller_input(event) == ApiControllerInput(
            path_parameters={}, body=""
        )

    @given(
        event=st.fixed_dictionaries(
            {
                "pathParameters": st.randoms(),
                "body": st.randoms(),
            }
        )
    )
    def test_given_expected_event(self, event: APIGatewayProxyEventV2) -> None:
        assert to_api_controller_input(event) == ApiControllerInput(
            path_parameters=event["pathParameters"], body=event["body"]
        )
