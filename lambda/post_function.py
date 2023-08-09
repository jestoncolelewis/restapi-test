import json

def handler(event, context):
    bodyID = event["body"]["bodyId"]
    bodyType = event["body"]["type"]
    bodyAmount = event["body"]["amount"]

    print("bodyID=" + bodyID)
    print("bodyType=" + bodyType)
    print("bodyAmount=" + bodyAmount)

    bodyResponse = {}
    bodyResponse["bodyID"] = bodyID
    bodyResponse["type"] = bodyType
    bodyResponse["amount"] = bodyAmount
    bodyResponse["message"] = "Hello from Lambdaland"

    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject["headers"] = {}
    responseObject["headers"]["ContentType"] = "applications/json"
    responseObject["body"] = json.dumps(bodyResponse)

    return responseObject
