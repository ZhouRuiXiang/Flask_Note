# -*- coding: utf-8 -*-#
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎来到首页！'


# 方法名称要大写
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 与前端约定，发送网络请求，不管验证是否成功（账号密码是否正确），都返回同样格式的JSON对象
        # {'code': 200, 'message': ''}
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'xingchen' and password == '111':
            # return '登录成功'
            return jsonify({'code': 200, 'message': ''})
        else:
            # return '登录失败'
            return jsonify({'code': 401, 'message': '用户名或密码错误！'})


if __name__ == '__main__':
    app.run(debug=True)
