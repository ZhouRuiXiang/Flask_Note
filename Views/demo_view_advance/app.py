from flask import Flask, views, jsonify, render_template, request
from functools import wraps

app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username and username == '星辰':
            return f(*args, **kwargs)
        else:
            return '请先登录'
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/settings/')
@login_required
def settings():
    return '设置页面'

# login_required(app.route('/settings/')(settings))
# ==
# @login_required
# @app.route('/settings/')

# app.route('/settings/')(login_required(settings))
# ==
# @app.route('/settings/')
# @login_required


class ProfileView(views.View):
    decorators = [login_required]

    def dispatch_request(self):
        return '个人中心页面'


app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))




class LoginView(views.MethodView):
    def __render(self, error=None):
        return render_template('login.html', error=error)


    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '星辰' and password == '123456':
            return '登录成功'
        else:
            return self.__render(error='用户名或密码错误！')


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))

# class JSONView(views.View):
#     def get_date(self):
#         raise NotImplementedError
#
#     def dispatch_request(self):
#         return jsonify(self.get_date())
#
#
# class ListView(JSONView):
#     def get_date(self):
#         return {'Mark': 19, 'Tony': 20}
#
#
# app.add_url_rule('/list/', view_func=ListView.as_view('list'))
#
#
# class AdvertiseView(views.View):
#     def __init__(self):
#         super(AdvertiseView, self).__init__()
#         self.context = {
#             'advertise': 'ICBC，爱存不存'
#         }
#
#
# class RegistView(AdvertiseView):
#     def dispatch_request(self):
#         self.context.update({
#             'name': '中国工商银行'
#         })
#         self.context['advertise'] = '想存就存'
#         return render_template('regist.html', **self.context)
#
#
# class LoginView(AdvertiseView):
#     def dispatch_request(self):
#         return render_template('login.html', **self.context)
#
#
# app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))
# app.add_url_rule('/login/', view_func=LoginView.as_view('login'))



if __name__ == '__main__':
    app.run()
