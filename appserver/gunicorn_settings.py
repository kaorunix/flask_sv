import os

bind = str(os.getenv('HOSTNAME'))+ ':' + str(os.getenv('PORT', 9876))
proc_name = 'Infrastructure-Practice-Flask'
workers = 4
