# -*- coding: utf-8 -*-#
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

user = User(username="小黄", password="123")
db.session.add(user)
# db.session.commit()

# 查询数据
# 在 session.query(tablename) == Cls.query
# users = User.query.order_by(User.id.desc()).all()
# 修改数据
# user = User.query.filter(User.id == 1).first()
# # user.username = "star"
# # db.session.commit()
# 删除数据
# user = User.query.filter(User.id == 2).first()
# db.session.delete(user)
# db.session.commit()


if __name__ == '__main__':
    app.run()
