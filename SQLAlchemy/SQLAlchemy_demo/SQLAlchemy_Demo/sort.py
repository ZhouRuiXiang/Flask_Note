# -*- coding: utf-8 -*-#

# Name:         sort.py
# Description:  
# Author:       Mark
# Date:         2019\8\8 0008 17:05
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime
import time

USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "sort"
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    # 使用default=datatime.now() 创建的对象时间会一样
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", backref=backref("my_articles", order_by=title.desc()))
    # __mapper_args__ = {
    #     "order_by": create_time.desc()
    # }

    def __repr__(self):
        return "<Article>title: %s, create_time: %s" % (self.title, self.create_time)

def db__init__():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    # user = User(username="小明")
    # article_1 = Article(title="test1")
    # user.my_articles=[article_1]
    # session.add(user)
    # session.commit()
    #
    # time.sleep(2)
    # article_2 = Article(title="test2")
    # user.my_articles.append(article_2)
    # session.commit()
    # user = session.query(User).first()
    # print(user.my_articles)
    for i in range(1, 101):
        title = "title: %s" % i
        article = Article(title=title)
        session.add(article)
    session.commit()

if __name__ == '__main__':
    # db__init__()
    # articles = session.query(Article).order_by("-create_time").all()
    # articles = session.query(Article).order_by(Article.create_time.desc()).all()
    # user = session.query(User).first()
    # print(user.my_articles)

    # db__init__()
    # article = session.query(Article).order_by(Article.id.desc()).limit(10).offset(5).all()
    article = session.query(Article).order_by(Article.title.desc())[: 10: -2]
    print(article)