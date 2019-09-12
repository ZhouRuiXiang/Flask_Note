# -*- coding: utf-8 -*-#

# Name:         group_byAndhaving.py
# Description:  
# Author:       Mark
# Date:         2019\8\9 0009 14:07
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, DateTime,Enum,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import enum
from datetime import datetime
import time

USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "onetomany"
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class genderEnum(enum.Enum):
    male = "male"
    female = "female"
    secret = "secret"


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    gender = Column(Enum(genderEnum), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return "<User>%s" % self.username


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    uid = Column(Integer, ForeignKey("user.id"), nullable=False)
    author = relationship("User", backref=backref("my_articles", lazy="dynamic", uselist="True"))

    def __repr__(self):
        return "<Article>%s" % self.title

def db_init_():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    user1 = User(username="小明", gender=genderEnum.male, age=18)
    for i in range(1):
        title = "title %s" % i
        article = Article(title=title)
        article.author = user1
        session.add(article)
    user2 = User(username="小花", gender=genderEnum.female, age=17)
    for i in range(1,6):
        title = "title %s" % i
        article = Article(title=title)
        article.author = user2
        session.add(article)
    user3 = User(username="小黑", gender=genderEnum.male, age=16)
    for i in range(6,9):
        title = "title %s" % i
        article = Article(title=title)
        article.author = user3
        session.add(article)
    user4 = User(username="小美", gender=genderEnum.female, age=19)
    user5 = User(username="小晴", gender=genderEnum.female, age=20)
    session.add_all([user1, user2, user3, user4, user5])
    session.commit()


if __name__ == '__main__':
    # db_init_()
    # 实现一个需求 查询与小明异性的朋友们的用户名、年龄，且年龄要大于18岁
    # 普通方法 需要查询两次 效率不高
    # ming = session.query(User.gender).filter(User.username=="小明").first()
    # result = session.query(User.username, User.age).filter(ming.gender != User.gender, User.age > 18).all()
    # print(result)
    # 子查询
    ming = session.query(User.gender.label("gender")).filter(User.username == "小明").subquery()
    result = session.query(User.username, User.age).filter(User.gender != ming.c.gender, User.age > 18).all()
    print(result)

    # 比如要实现一个需求，查找所有用户，按照用户发表文章的数量来进行排序。
    # result = session.query(User.username, func.count(Article.id)).join(Article,
    #     User.id==Article.uid).group_by(User.id).order_by(func.count(Article.id).desc()).all()
    # print(result)

