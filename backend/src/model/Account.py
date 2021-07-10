from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Status
import sqlalchemy
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
    created_by = Column(Integer)
    created_at = Column(Timestamp)
    updated_by = Column(Integer)
    updated_at = Column(Timestamp)
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
            "id" : self.account_id,
            "account_name" : self.account_name,
            "start_on" : self.start_on, 
            "end_on" : self.end_on,
            "created_by" : self.created_by,
            "created_at" : self.created_at, 
            "updated_by" : self.updated_by,
            "updated_at" : self.updated_at,
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
    res = ses.query(Account).filter(Account.id==account_id).all()
    ses.close()
    # 返却されるレコードは１件だが配列のまま返すことでエラーハンドリングを受け手に任せる
    return res

def search(account_dict, operation_account_id):
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

    ses.close()
    return res
            

        #v = account_dict.get('account_name')
#    if (v != None):
#        rs = work_query.filter(Account.account_name==v)
#    v = account_dict.get('start_on')
#    if (v != None):
#        work_query = work_query.filter(Account.start_on==v)
#    v = account_dict.get('end_on')
#    if (v != None):
#        work_query = work_query.filter(Account.end_on==v)
#    v = account_dict.get('created_by')
#    if (v != None):
#        work_query = work_query.filter(Account.created_by==v)
#    v = account_dict.get('created_at')
#    if (v != None):
#        work_query = work_query.filter(Account.created_at==v)
#    v = account_dict.get('updated_at')
#    if (v != None):
#        work_query = work_query.filter(Account.updated_at==v)
#    v = account_dict.get('updated_by')
#    if (v != None):
#        work_query = work_query.filter(Account.updated_by==v)
#    v = account_dict.get('status')
#    if (v != None):
#        work_query = work_query.filter(Account.status==v)
#    res = work_query.all()
#    ses.close()
#    return res
    

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

def update(account, operation_account_id):
    id = account['id']
    account_name = account['account_name']
    start_on = account['start_on']
    end_on = account['end_on']
    updated_by = operation_account_id
    updated_at = datetime.datetime.now()
    
