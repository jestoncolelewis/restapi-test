from aws_cdk import (
    Stack,
    aws_lambda as alamb,
    aws_apigatewayv2_alpha as api
)
from constructs import Construct

class RestapiTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        get_function = alamb.Function(
            self, "GetFunction",
            runtime=alamb.Runtime.PYTHON_3_9,
            code=alamb.Code.from_asset("lambda"),
            handler="get_function.handler"
            )
        get_url = get_function.add_function_url()

        post_function = alamb.Function(
            self, "PostFunction",
            runtime=alamb.Runtime.PYTHON_3_9,
            code=alamb.Code.from_asset("lambda"),
            handler="post_function.handler"
        )
        options_function = alamb.Function(
            self, "OptionsFunction",
            runtime=alamb.Runtime.PYTHON_3_9,
            code=alamb.Code.from_asset("lambda"),
            handler="options_function.handler"
        )
