# -*- coding: utf-8 -*-#
from flask import Flask,url_for
from flask_restful import Api, Resource, reqparse, inputs, marshal_with, fields
import config
from exts import db
from models import User, Article, Tag
from articleViews import article_bp


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
api = Api(app=app)
app.register_blueprint(article_bp)

@app.route('/')
def index():
    article = Article(title="Python_study", content="SQLAlchemy, Jinjia, werkzeug")
    user = User(username="xingchen", gender="male", email="1215686977@qq.com")
    article.author = user
    # print(type(article.tags))
    tag1 = Tag(name="Python")
    tag2 = Tag(name="Flask")
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return "欢迎来到首页！"


class LoginView(Resource):
    resource_fields = {
        # attribut='uid'必须对应ORM模型User中的uid字段，若该字段不存在，则返回给前端的JSON数据uid值为null
        # 'id': fields.String(attribute='uid'),     #错误写法
        'uid': fields.String(attribute='id'),
        'username': fields.String(),
        'gender': fields.String(default='male')
    }

    @marshal_with(resource_fields)
    def get(self, user_id=1):
        user = User.query.get(user_id)
        return user

    # username=None 形参设置为None 可以避免无参url访问404的问题
    def post(self, username=None):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, type=str, help='用户名验证错误！')
        parser.add_argument('password', required=True, type=str, help='密码验证错误！')
        parser.add_argument('age', type=int, help='年龄必须为整数！')
        # 日期格式为 xxxx-xx-xx
        parser.add_argument('birthday', type=inputs.date, help='您输入的格式不正确！')
        parser.add_argument('telephone', type=inputs.regex(r'1[35678]\d{9}'), help='手机号码输入不正确！')
        args = parser.parse_args()
        print(args)
        return {'username': username}


# 这里是用绑定app的api对象来调用add_resource()方法
api.add_resource(LoginView, '/login/<user_id>/', '/login/<username>/', '/login/', endpoint='login')

with app.test_request_context():
    print(url_for('login'))



if __name__ == '__main__':
    app.run()
