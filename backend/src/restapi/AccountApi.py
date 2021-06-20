from model import Account
#from __future__ import absolute_import, unicode_literals 
import json
import datetime
#import requests

def getById(account_id, user_id):
    """
    /account/get/<id>で呼び出されたAPIの検索処理

    Parameters
    ----------
    account_id : int
        検索するアカウントのアカウントID
    user_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    ret
        json形式のアカウント詳細
    {
      "body": {
        "name": "account",
        "id": <account_id>,
        "account_name": <account_name>,
        "start_on": "2021-01-01 10:00:00",
        "end_on": "2025-12-31 21:00:00"
    },
      "status": {
        "code" : "I0001",
        "message" : "",
        "detail" : ""
      }
    }
    """
    
    result = Account.getById(account_id, user_id)
    # TODO モデルの検索結果(正常・異常)によってレスポンスの出力内容を替える
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


def create(account_request, user_id):
    """
    /account/createで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_request : json
        作成するアカウント詳細
    user_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """
    
    data = account_request.data.decode('utf-8')
    date = json.loads(data)
    account = {
        'account_name' : str(account_request['account_name']),
        'start_on' : str(account_request['start_on']),
        'end_on' : str(account_request['end_on'])
    }
    message=""
    code=""
    try:
        if Account.create(account, user_id) == True:
            code="I0001"
        
    except:
        code="E0009"
        message="Created failed"
    
    result = Account.getById(account_id, user_id)
    result_json = {
        "body": "",
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    ret = json.dumps(result_json)
    return ret
