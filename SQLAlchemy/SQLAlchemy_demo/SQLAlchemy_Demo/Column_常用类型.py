# -*- coding: utf-8 -*-#

# Name:         Column_常用类型.py
# Description:  
# Author:       Mark
# Date:         2019\8\2 0002 13:55

from sqlalchemy import create_engine,Column,String,Integer,Float,Boolean,DECIMAL,Enum,Date,Time,DateTime,Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
import enum
from datetime import datetime
from datetime import date
from datetime import time
# 定义DB_URI
# dialect+driver://username:password@host:port/database?charset=utf8
USERNAME = "root"
PASSWORD = "286977"
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "test_column"
#         mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8
DB_URI = "mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8"\
    .format(user=USERNAME, passwd=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)
# 创建数据库引擎，连接数据库
engine = create_engine(DB_URI)
# 构建基类
Base = declarative_base(engine)
# 创建会话
session = sessionmaker(bind=engine)()

class BankTypeEnum(enum.Enum):
    CCB = "CCB"
    ABC = "ABC"
    ICBC = "ICBC"


class Bank_save(Base):
    # 定义表名
    __tablename__ = "bank_save"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(100))
    # price = Column(Float)
    # is_delete = Column(Boolean)
    price = Column(DECIMAL(8, 6))
    card_type = Column(Enum(BankTypeEnum))
    create_time = Column(Date)
    article = Column(LONGTEXT)


    def __init__(self, name, price, card_type, create_time, article):
        self.name = name
        self.price = price
        # self.is_delete = is_delete
        self.card_type = card_type
        self.create_time = create_time
        self.article = article


Base.metadata.drop_all()

Base.metadata.create_all()
# 出现精度问题
data = Bank_save(name="Mark", price=99.999999, card_type=BankTypeEnum.CCB, create_time=date(2019, 8, 2), article="aaaaa")
session.add(data)
try:
    session.commit()
except Exception as e:
    print(e)










