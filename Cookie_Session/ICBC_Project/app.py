# -*- coding: utf-8 -*-#
from flask import Flask, render_template, views, request, session
from exts import db
import config
from models import User
from forms import RegistForm, LoginForm, TransferForm
from auth import login_required
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


class RegistView(views.MethodView):
    def get(self):
        return render_template('regist.html')

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
            user = User(email= email, username=username, password=password, deposit=deposit)
            db.session.add(user)
            db.session.commit()
            return "注册成功"
        else:
            print(form.errors)
            return "注册失败"


class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            # 查询一定要有'.first()' 否则返回的是Query()对象
            user = User.query.filter(User.email == email, User.password == password).first()
            if not user:
                return "邮箱或密码不正确，请重新输入！"
            else:
                session['user_id'] = user.id
                return "登录成功！"


class TransferView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('transfer.html')

    def post(self):
        form = TransferForm(request.form)
        print(session.get('csrf_token'))
        if form.validate():
            email = form.email.data
            amount = form.amount.data
            user = User.query.filter_by(email=email).first()
            if user:
                user_id = session.get('user_id')
                myself = User.query.filter(User.id == user_id).first()
                if myself.email == email:
                    return "转入账户不能为自身！"
                if myself.deposit >= amount:
                    myself.deposit -= amount
                    user.deposit += amount
                    db.session.commit()
                    return "转账成功！"
                else:
                    return "余额不足！"
            else:
                return "您输入的邮箱不正确！"
        else:
            return '您输入的数据格式不正确！'


app.add_url_rule("/regist/", view_func=RegistView.as_view('regist'))
app.add_url_rule("/login/", view_func=LoginView.as_view('login'))
app.add_url_rule("/transfer/", view_func=TransferView.as_view('transfer'))

if __name__ == '__main__':
    app.run()
