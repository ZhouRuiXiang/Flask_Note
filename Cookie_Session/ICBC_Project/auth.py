# -*- coding: utf-8 -*-#

# Name:         auth.py
# Description:  
# Author:       Mark
# Date:         2019\8\23 0023 13:34

from functools import wraps
from flask import session
from flask import redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
