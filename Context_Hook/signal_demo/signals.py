# -*- coding: utf-8 -*-#

# Name:         signals.py
# Description:  
# Author:       Mark
# Date:         2019\8\28 0028 15:09


from blinker import Namespace
from datetime import datetime
from flask import request
namespace = Namespace()

login_signal = namespace.signal('login')


def login_log(sender, username):
    ip = request.remote_addr
    now = datetime.now()
    log_line = '{username}*{now}*{ip}'.format(username=username, now=now, ip=ip)
    with open('signal_demo\login_logs.txt', 'a')as f:
        f.write(log_line+"\n")


login_signal.connect(login_log)



