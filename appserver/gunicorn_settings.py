import os

bind = str(os.getenv('HOSTNAME'))+ ':' + str(os.getenv('PORT', 8080))
proc_name = 'Infrastructure-Practice-Flask'
workers = 4

# access log
accesslog = '/home/ec2-user/Projects/flask_sv/appserver/log/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn log
errorlog = '-'
loglevel = 'info'
