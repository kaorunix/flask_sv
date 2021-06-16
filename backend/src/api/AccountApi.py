from model import Account
import json
import datetime

def getById(account_id, user_id):
    result = Account.getById(account_id, user_id)
    result_json = {
        "body": {
            "name": "account",
            "id": account_id,
            "account_name": result[0].account_name,
            "start_on": result[0].start_on.strftime("%Y-%m-%d %H:%M:%S"),
            "end_on": result[0].end_on.strftime("%Y-%m-%d %H:%M:%S")
        },
        "status": {
            "code" : "I0001",
            "message" : "",
            "detail" : ""
        }
    }
    ret = json.dumps(result_json)
    return ret
