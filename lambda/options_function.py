import json

def handler(event, context):
    print(type(event))
    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = "applications/json"
    responseObject["headers"]["Access-Control-Allow-Headers"] = "Content-Type"
    responseObject["headers"]["Access-Control-Allow-Origin"] = "*"
    responseObject["headers"]["Access-Control-Allow-Methods"] = "OPTIONS,POST,GET"
    responseObject["body"] = event

    return responseObject