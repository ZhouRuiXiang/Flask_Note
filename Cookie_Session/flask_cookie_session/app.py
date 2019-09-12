# -*- coding: utf-8 -*-#
from flask import Flask, request, Response
from datetime import datetime
from subViews import bp
app = Flask(__name__)
app.register_blueprint(bp)
app.config["SERVER_NAME"] = "test.com:5000"


@app.route('/')
def hello_world():
    resp = Response("Hello World!")
    # max_age 以秒为单位，距离现在多少秒后过期
    # resp.set_cookie(key="username", value="xingchen", max_age=100)
    # expires datetime类型 设置的时间是Greenwich Mean Time（格林威治时间/格林尼治时间）
    # 格林威治时间 + 8小时 = 东八区时间
    # expires虽然在http协议是被废弃了，但是到目前为止，所有的浏览器还是都支持
    # max_age在IE8以下的浏览器是不支持的
    expires = datetime(year=2019, month=8, day=22, hour=9, minute=14, second=20)
    # resp.set_cookie(key="username", value="xingchen", expires=expires)
    # 若max_age和expires都指定，则默认使用max_age参数的值
    resp.set_cookie(key="username", value="xingchen", max_age=600, expires=expires, domain=".test.com")
    return resp


@app.route('/del/')
def delCookie():
    resp = Response("删除cookie")
    resp.delete_cookie(key="username")
    return resp


if __name__ == '__main__':
    app.run()
