from model import db
from model import Account
from model import Status
from restapi import AccountApi
import pprint
import datetime
import ujson
import requests

def test_getById():
    """
    restapi/getById
    """
    account = {
        'account_name' : 'flask_sv',
        'start_on' : '2021-05-05 00:00:00',
        'end_on' : '2030-12-31 00:00:00'
    }

    Account.create(account, 999) == True

    account_dict = {
        'account_name' : "flask_sv",
        'end_on' : "2030-12-31 00:00:00"
    }
    result = Account.search(account_dict, 1)
    result_id = result[0].id
    result_json = AccountApi.getById(result_id, 100)
    print(f"json: {AccountApi.getById(result_id, 100)}")

    assert result_json == """{"body": {"name": "account", "id": """+str(result_id)+""", "account_name": "flask_sv", "start_on": "2021-05-05 00:00:00", "end_on": "2030-12-31 00:00:00"}, "status": {"code": "I0001", "message": "", "detail": ""}}"""

def test_account_get():
    """
    """
    # modelから試験データ登録
    test_account_name = 'api_account_get'
    account = {
        'account_name' : test_account_name,
        'start_on' : '2021-06-23 00:00:00',
        'end_on' : '2030-12-31 00:00:00'
    }

    Account.create(account, 999) == True

    account_dict = {
        'account_name' : test_account_name
    }
    result = Account.search(account_dict, 999)
    account_id = result[0].id

    # APIから確認
    url = f"http://localhost:5000/account/get/{account_id}"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.get(url, headers=headers)
    # HTTP Statusコードが200であること
    assert response.status_code == 200

    # BODYをjsonでパースできること
    data = ujson.loads(response.text)

    # 配列内にurl, state, created_atの要素が存在すること
    assert 'body' in data
    assert 'status' in data
