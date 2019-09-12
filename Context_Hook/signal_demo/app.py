# -*- coding: utf-8 -*-#
from flask import Flask, request,template_rendered,render_template, got_request_exception
from signals import login_signal
app = Flask(__name__)


# def template_rendered_func(sender, template, context):
#     print("sender: ", sender)
#     print("template: ", template)
#     print("context: ", context)


# template_rendered.connect(template_rendered_func)

def request_exception_log(sender, *args, **kwargs):
    # 可以保存异常的log
    print("sender: ", sender)
    print(args)
    print(kwargs)

got_request_exception.connect(request_exception_log)



@app.route('/')
def hello_world():
    # a = 1 / 0
    print(a)
    return render_template("test.html")


@app.route('/login/')
def login():
    username = request.args.get('username')
    if username:
        login_signal.send(username=username)
        return '登录成功！'
    else:
        return '请输入用户名！'

if __name__ == '__main__':
    app.run()
