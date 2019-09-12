# -*- coding: utf-8 -*-#

# Name:         relationship_cascade.py
# Description:  
# Author:       Mark
# Date:         2019\8\8 0008 13:34
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


# DB_URI = "dialect+driver://username:passwrod@host:port/database?charset=utf8"
USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "user_article"
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    # my_article =relationship("Article", cascade="save-update,delete")


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))
    author = relationship("User", backref=backref("my_articles", cascade="save-update,delete"), cascade="save-update,delete")


class Comments(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))

    author = relationship("User", backref=backref("my_comments"))


def db__init__():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    user = User(username="小明")
    article = Article(title="我爱你中国")
    comment = Comments(content="拔刀吧，情敌", uid=1)
    user.my_comments.append(comment)
    user.my_articles.append(article)
    session.add(user)
    session.commit()


def operations():
    user = session.query(User).first()
    session.delete(user)
    session.commit()


if __name__ == '__main__':
    db__init__()
    # operations()