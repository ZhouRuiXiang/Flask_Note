# -*- coding: utf-8 -*-#

# Name:         SQLAlchemy_mappings.py
# Description:  
# Author:       Mark
# Date:         2019\7\31 0031 16:17

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "first_sqlalchemy"
USERNAME = "root"
PASSWORD = "286977"

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE
)
engine = create_engine(DB_URI)
# 构造一个基类
Base = declarative_base(engine)
# 1. 创建一个ORM模型，这个ORM模型必须继承自sqlalchemy给我们提供好的基类


class Person(Base):
    # 定义表名
    __tablename__ = "person"
    # 2. 在ORM模型中定义一些属性，跟表中的字段作映射。这些属性必须是sqlalchemy提供的数据类型
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    reigon  = Column(String(100))

    # 调用__str__来打印Person()对象
    def __init__(self, name, age, reigon):
        self.name = name
        self.age = age
        self.reigon = reigon

    def __str__(self):
        # print()
        return self.name, self.age, self.reigon

    def __repr__(self):
        return "{}".format({"name": self.name, "age": self.age, "reign": self.reigon})

    def getDB_URI(self):
        return DB_URI


# 3. 将创建好的数据模型映射到数据库中
Base.metadata.create_all()
if __name__ == '__main__':
    # 创建一条数据
    p = Person(name="CHEN", age=18, reigon="Hubei")

# P = repr(p)
# print(P)




