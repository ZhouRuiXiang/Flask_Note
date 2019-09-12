# -*- coding: utf-8 -*-#

# Name:         Column_commonParameters.py
# Description:  
# Author:       Mark
# Date:         2019\8\2 0002 17:01


from sqlalchemy import create_engine,Column,String,Integer,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from datetime import datetime
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


class Book(Base):
    # 定义表名
    __tablename__ = "book"
    id = Column(Integer, autoincrement=True, primary_key=True)
    # create_time = Column(DateTime, default=datetime.now())
    description = Column(String(100), name="描述", nullable=True)
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self,description):
        # self.create_time = create_time
        self.description = description
        pass


Base.metadata.drop_all()
Base.metadata.create_all()
book = Book("abcd")
session.add(book)
# book = session.query(Book).first()
# book.description="aaa"
if __name__ == '__main__':
    try:
        session.commit()
    except Exception as e:
        print(e)
