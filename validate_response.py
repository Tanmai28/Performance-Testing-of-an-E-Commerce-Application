import json

def validate(response_json):
    try:
        data = json.loads(response_json)
        return "status" in data and "message" in data
    except:
        return False


print(validate('{"status":"ok","message":"success"}'))
