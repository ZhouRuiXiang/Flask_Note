# -*- coding: utf-8 -*-#
from flask import Flask, url_for, current_app, request, session, render_template
from flask import g
from utils import log_a,log_b
import os
from flask import abort

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)


app_context = app.app_context()
app_context.push()

# 每一次请求视图函数之前
@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = "xingchen"


@app.route('/')
def hello_world():
    # print(current_app.name)
    # username = request.args.get('username')
    # g.username = username
    # log_a()
    # log_b()
    print(g.usdfas)
    if hasattr(g, 'user'):
        print(g.user)
    return render_template("index.html")


@app.route('/list/')
def my_list():
    session['user_id'] = 1
    # abort(404)
    return render_template("list.html")


# 钩子函数（装饰器）
# @app.before_first_request
# def before_first_request():
#     print("第一次请求")

@app.context_processor
def context_processor():
    # 一定要有return 若不写else 则默认 return None
    # return {'cur_user': 'xingchen'} / return {}
    if hasattr(g, 'user'):
        return {'cur_user': 'xingchen'}
    else:
        return {}


@app.errorhandler(AttributeError)
def server_error(error):
    # render_template()后接状态码表示返回相应的状态码，否则返回200状态码
    return render_template('500.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



# with app.test_request_context():
#     print(url_for('my_list'))
# print(current_app.name)

if __name__ == '__main__':
    app.run(debug=True)






