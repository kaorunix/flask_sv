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
               
def test_create():
    """
    """
    account = {
        'account_name' : 'flask sv',
        'start_on' : '2021-05-05 00:00:00',
        'end_on' : '2030-12-31 00:00:00',
    }

    Account.create(account, 999)


def test_update():
    """
    """
    account = {
        'account_name' : 'update',
        'start_on' : '2021-05-03 00:00:00',
        'end_on' : '2031-12-31 00:00:00',
    }
    Account.create(account, 999)
    account_created1 = Account.search('update', 999)
    print(account_created1)

    search_cond = {
        'account_name': 'update',
        'start_on' : '2021-05-03 00:00:00',
        'end_on' : '2031-12-31 00:00:00',
    }
    account_created = Account.search('update', 999)[0].toDict()
    assert account_created['account_name'] == 'update'
    assert account_created['start_on'] == '2021-05-03 00:00:00'
    assert account_created['end_on'] == '2031-12-31 00:00:00'

    
    account = {
        'id' : account_updated['id'],
        'end_ion': '2035-12-31 12:00:00'
    }
    assert Account.update(account, 999) == True
    search_cond = {
        'account_name': 'update',
        'end_on' : '2035-12-31 12:00:00'
    }
    account_updated = Account.search(search_cond, 999)[0].toDict()
    assert account_updated['account_name'] == 'update'
    assert account_updated['start_on'] == '2021-05-03 00:00:00'
    assert account_updated['end_on'] == '2035-12-31 00:00:00'
