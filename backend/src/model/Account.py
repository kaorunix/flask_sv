from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Status
import sqlalchemy
from model.common import strftime
from model.common import strptime
#from sqlalch

import datetime
from datetime import datetime

from model.db import engine
from model.db import Base

# model class
class Account(Base):
    """
    accountモデル
    flask_svシステムにログインするアカウントを管理するモデル

    Parameters
    ----------
    Base : データベース接続子
    """
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    account_name = Column(String())
    start_on = Column(Timestamp)
    end_on = Column(Timestamp)
    created_by = Column(Integer, nullable=True)
    created_at = Column(Timestamp, nullable=True)
    updated_by = Column(Integer, nullable=True)
    updated_at = Column(Timestamp, nullable=True)
    status = Column(Integer)

    # get Dict data
    def toDict(self):
        """
        ディクショナリ形式でクラスの全メンバを返却する

        Parameters
        ----------
        self : 自クラス

        Returns
        -------
        クラスの全メンバのディクショナリ
        """
        return {
            'id' : int(self.id),
            'account_name' : str(self.account_name),
            'start_on' : str(self.start_on), 
            'end_on' : str(self.end_on),
            'created_by' : int(self.created_by),
            'created_at' : str(self.created_at), 
            'updated_by' : int(self.updated_by),
            'updated_at' : str(self.updated_at),
            'status' : Status.getStatusName(str(self.status))
        }
    # datetime.strptime(str(self.start_on), "%Y-%m-%d %H:%M:%S")

    def toJson(self):
        return {
            "name": "account",
            "id" : str(self.id),
            "account_name" : self.account_name,
            "start_on" : strftime(self.start_on), 
            "end_on" : strftime(self.end_on),
            "created_by" : str(self.created_by),
            "created_at" : strftime(self.created_at), 
            "updated_by" : str(self.updated_by),
            "updated_at" : strftime(self.updated_at),
            "status" : Status.getStatusName(str(self.status))
        }
    
# get List data    
def getByList(arr):
    res = []
    for item in arr:
        res.append(item.toDict())
    return res

# get all mydata record
def getAll():
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(Account).all()
    ses.close()
    return res


def getById(account_id, operation_account_id):
    """
    アカウントidでaccountテーブルを検索をし、該当したAccountオブジェクト群を取得する

    Parameters
    ----------
    account_id : 検索対象のアカウントid
    operation_account_id : 操作ユーザーのアカウントid

    Returns
    -------
    Accountオブジェクトのリスト
    """
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(Account).get(account_id)
    ses.close()
    return res

def search(account_dict, operation_account_id):
    """
    dictアカウントからaccountテーブルを検索し、該当したAccountオブジェクト群を取得する

    Parameters
    ----------
    {
        'account_name' : 文字列str(self.account_name),
        'start_on' : 文字列 '2020-05-01 00:00:00',
        'end_on' : 文字列 '2020-12-31 00:00:00',
        'created_by' : account_id,
        'created_at' : 文字列 '2020-12-31 00:00:00',
        'updated_by' : account_id,
        'updated_at' : 文字列 '2020-12-31 00:00:00',
        'status' : statusの数値
    }

    Returns
    -------
    Accountオブジェクトのリスト
    """
    print(f"account_dict={account_dict}")
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = None
    rs = ses.query(Account)
    v = account_dict.get('account_name')
    if (v != None):
        rs = rs.filter(Account.account_name==v)
    v = account_dict.get('start_on')
    if (v != None):
        rs = rs.filter(Account.start_on==v)
    v = account_dict.get('end_on')
    if (v != None):
        rs = rs.filter(Account.end_on==v)
    v = account_dict.get('created_by')
    if (v != None):
        rs = rs.filter(Account.created_by==v)
    v = account_dict.get('created_at')
    if (v != None):
        rs = rs.filter(Account.created_at==v)
    v = account_dict.get('updated_by')
    if (v != None):
        rs = rs.filter(Account.updated_by==v)
    v = account_dict.get('updated_at')
    if (v != None):
        rs = rs.filter(Account.updated_at==v)
    v = account_dict.get('status')
    if (v != None):
        rs = rs.filter(Account.status==v)

    res = rs.all()
    print(f"res={res}")
    ses.close()
    return res
            
def create(account_dict, operation_account_id):
    account = Account()
    account.account_name = account_dict['account_name']
    account.start_on = account_dict['start_on']
    account.end_on = account_dict['end_on']
    account.created_by = operation_account_id
    account.created_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    account.updated_by = sqlalchemy.null()
    account.updated_at = sqlalchemy.null()
    account.status = Status.getStatusKey("NEW")
    Session = sessionmaker(bind=engine)
    ses = Session()
    ses.begin()
    try:
        ses.add(account)
        ses.commit()
        res = True
    except:
        ses.rollback()
        res = False
    finally:
        ses.close()
    return res

def update(account_dict, operation_account_id):
    account_id = account_dict.get('id')
    Session = sessionmaker(bind=engine)
    res=False
    ses = Session()
    account_record = ses.query(Account).get(account_id)
    try:
        v = account_dict.get('account_name')
        if (v != None):
            account_record.account_name=v
        v = account_dict.get('start_on')
        if (v != None):
            account_record.start_on=v
        v = account_dict.get('end_on')
        if (v != None):
            account_record.end_on=v
        account_record.updated_by=operation_account_id
        account_record.updated_at=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        v = account_dict.get('status')
        if (v != None):
            account_record.status=v
        ses.commit()
        res = True
    except:
        ses.rollback()
        res = False
    finally:
        ses.close()
    return res    
    
