from aws_cdk import (
    Stack,
    aws_lambda as alamb,
    aws_apigateway as api
)
from constructs import Construct

class RestapiTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        function = alamb.Function(
            self, "Function",
            runtime=alamb.Runtime.PYTHON_3_9,
            code=alamb.Code.from_asset("lambda"),
            handler="function.handler"
            )

        rest_api = api.LambdaRestApi(
            self, "REST",
            handler=function,
            proxy=True
        )
        functions = rest_api.root.add_resource("functions")
        functions.add_method("GET")
        functions.add_method("POST")
