# 0. NEW
# 1. ACTIVE
# 2. INACTIVE
# 3. DELETE

status_dict = {
    '0':'NEW',
    '1':'ACTIVE',
    '2':'INACTIVE',
    '3':'DELETE'
}

def getName(key, dict):
    dict.get(key, "ERROR")

def getStatusName(key):
    getName(key, status_dict)

def getValue(value, dict):
    keys = [k for k, v in dict.items() if v == value]
    if (keys.len() == 1):
        return int(keys[0])
    else:
        return -1
   
def getStatusValue(value):
    getValue(value, status_dict)
    
# 0. NOT_APPROVED
# 1. APPROVED

def getApprovalName(status):
    if status == 0:
        return "NOT_APPROVED"
    elif status == 1:
        return "APPROVED"
    else:
        return "ERROR"

    
