from model import Account
#from __future__ import absolute_import, unicode_literals 
import json
import datetime
#import requests

def getById(account_id, operation_account_id):
    """
    /account/get/<id>で呼び出されたAPIの検索処理

    Parameters
    ----------
    account_id : int
        検索するアカウントのアカウントID
    operation_account_id : int
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
    
    result = Account.getById(account_id, operation_account_id)
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


def create(account_request, operation_account_id):
    """
    /account/createで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_request : json
        作成するアカウント詳細
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    print(account_request)
    account_request = json.loads(account_request)
    account = {
        'account_name' : str(account_request['account_name']),
        'start_on' : str(account_request['start_on']),
        'end_on' : str(account_request['end_on'])
    }
    message=""
    code=""
    try:
        if Account.create(account, operation_account_id) == True:
            code="I0001"
            message="Created Account Succesfuly."
        else:
            code="E0001"
            message=""
        
    except:
        code="E0009"
        message="Created failed"
    

#    result = Account.getById(account_id, operation_account_id)
    result_json = {
        "body": "",
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    ret = result_json
    return ret


def search(account_request, user_id):
    """
    /account/searchで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_request : json
        アカウント検索項目
    user_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    print(account_request)
    account_request = json.loads(account_request)
#    account = {
#        'account_name' : str(account_request['account_name']),
#        'start_on' : str(account_request['start_on']),
#        'end_on' : str(account_request['end_on']),
#        'created_by' : int(account_request['created_by']),
#        'created_at' : str(account_request['created_at']),
#        'updated_by' : int(account_request['updated_by']),
#        'updated_at' : str(account_request['updated_at']),
#        'status' : int(account_request['status'])
#    }
    message=""
    code=""
    try:
        results = Account.search(account_request, user_id)
        code="I0001"
        
        message=f"Found ({results.length}) records."
        
    except:
        code="E0009"
        message="Search failed"
    
#    result = Account.getById(account_id, user_id)
    result_json = {
        "body": [ lambda s: s.toJson(), results 
        ],
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    ret = result_json
    return ret
