# -*- coding: utf-8 -*-#

# Name:         models.py
# Description:  
# Author:       Mark
# Date:         2019\8\13 0013 14:03
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "alembic_demo"
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(bind=engine)
# ORM模型 -> 迁移脚本（中间件） -> 映射到数据库中


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(20), nullable=False)
    gender = Column(Enum("male", "female"))
    age = Column(Integer)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)
    author = relationship("User", backref="my_articles")





