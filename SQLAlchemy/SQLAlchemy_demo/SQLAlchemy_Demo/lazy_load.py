# -*- coding: utf-8 -*-#

# Name:         lazy_load.py
# Description:  
# Author:       Mark
# Date:         2019\8\9 0009 12:15
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
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
    author = relationship("User", backref=backref("my_articles", order_by=id.desc()))

    def __repr__(self):
        return "<Article>%s, %s" % (self.id, self.title)



# Base.metadata.drop_all()
# Base.metadata.create_all()
# user = User(username="小明")
# for i in range(100000):
#     title = "%s" % i
#     article = Article(title=title)
#     article.author = user
#     session.add(article)
# session.commit()


if __name__ == '__main__':
    user = session.query(User).first()
    # lazy_load
    # start = time.perf_counter()
    # print(user.my_articles.filter(Article.id == 50000).all())
    # print("{:.10f}".format(time.perf_counter()-start))


    # general
    print(type(user.my_articles))
    start2 = time.perf_counter()
    for article in user.my_articles:
        if article.id == 50000:

            print(article)
    print("{:.10f}".format(time.perf_counter() - start2))

