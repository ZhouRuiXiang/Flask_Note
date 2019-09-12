# -*- coding: utf-8 -*-#
from flask import Flask, session
import os
from datetime import timedelta
app = Flask(__name__)
app.config.update({
    'SECRET_KEY': os.urandom(24),
    # 将session到期时间改为2天后
    'PERMANENT_SESSION_LIFETIME': timedelta(days=2)
})

@app.route('/')
def index():
    # 设置session
    session['username'] = 'xingchen'
    # permanent 持久化
    # session.permanent = True 默认时间为31天
    session.permanent = True
    return 'Hello World!'

@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return username or "没有获取到session"

@app.route('/delete_session/')
def delete_session():
    # session.pop('username')
    session.clear()
    return "删除成功"
if __name__ == '__main__':
    app.run()
