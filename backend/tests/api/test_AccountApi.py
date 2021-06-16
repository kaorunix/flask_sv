from model import db
from model import Account
from model import Status
from api import AccountApi
import pprint
import datetime

def test_getById():
    """
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
    result_json = AccountApi.getById(result[0].id, 100)
    print(f"json: {AccountApi.getById(result[0].id, 100)}")

    assert result_json == """{"body": {"name": "account", "id": 45, "account_name": "flask_sv", "start_on": "2021-05-05 00:00:00", "end_on": "2030-12-31 00:00:00"}, "status": {"code": "I0001", "message": "", "detail": ""}}"""

#    assert result[0].account_name == account_dict['account_name'] 
#    assert result[0].start_on == datetime.datetime.strptime(account['start_on'], '%Y-%m-%d %H:%M:%S')
#    assert result[0].end_on == datetime.datetime.strptime(account_dict['end_on'], '%Y-%m-%d %H:%M:%S')
#    assert result[0].created_by == 999
#    assert result[0].status == Status.getStatusKey("NEW")

