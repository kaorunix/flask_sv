from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Status
#from sqlalch

import datetime
from datetime import datetime

from model.db import engine
from model.db import Base

# model class
class Account(Base):
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


def getById(id, user_id):
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(Account).filter(Account.id==id).all()
    ses.close()
    # 返却されるレコードは１件だが配列のまま返すことでエラーハンドリングを受け手に任せる
    return res


def create(account, user_id):
    account_name = account['account_name']
    start_on = account['start_on']
    end_on = account['end_on']
    created_by = user_id
    created_at = datetime.datetime.now()
    updated_by = NULL
    updated_at = NULL
    status = Status.getStatusValue("NEW")

def update(account, user_id):
    id = account['id']
    account_name = account['account_name']
    start_on = account['start_on']
    end_on = account['end_on']
    updated_by = user_id
    updated_at = datetime.datetime.now()
    
