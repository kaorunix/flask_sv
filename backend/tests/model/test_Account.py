from model import db
from model import Account
import pprint

def test_getById():
    """
    """
    user_id = 1
    id = 1
    accounts = Account.getById(id, user_id)
    assert len(accounts) == 1
    pprint.pprint(accounts)
    account = accounts[0].toDict()
    assert account['id'] == 1
    assert account['account_name'] == 'ksato'
    assert account['start_on'] == '2021-04-25 15:08:02'
    assert account['end_on'] == '2030-12-31 00:00:00'
    assert account['created_by'] == 1
#    assert account['created_at'] == ''
    assert account['updated_by'] == 1
#    assert account['updated_at'] == ''
#    assert account['status'] == 1
               
