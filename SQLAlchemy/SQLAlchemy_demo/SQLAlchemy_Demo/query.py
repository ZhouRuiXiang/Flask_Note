# -*- coding: utf-8 -*-#

# Name:         query.py
# Description:  
# Author:       Mark
# Date:         2019\8\6 0006 14:30

from sqlalchemy import create_engine,Column,Integer,String,Enum,func,and_,or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import enum
# 定义DB__URI
# dialect+driver://username:password@host:port/database?charset=utf8
USERNAME = "root"
PASSWORD = "286977"
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "test_query"
DB_URI = "mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8"\
    .format(user=USERNAME, passwd=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)
# 构建基类
Base = declarative_base(bind=engine)
# 创建会话
session = sessionmaker(bind=engine)()


class genderEnum(enum.Enum):
    male = "Male"
    female = "Female"
# League of legends


class LOL(Base):
    # 写表名
    __tablename__ = "LOL_Hero"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=True)
    gender = Column(Enum(genderEnum), default="Male")
    hp = Column(Integer)
    def __repr__(self):
        return "<LOL>id:%d name:%s" % (self.id, self.name)

# 删除表
# Base.metadata.drop_all()

# 创建表
# Base.metadata.create_all()

if __name__ == '__main__':
    HERO = ["Galen", "Jiawen IV", "Rui Wen", "Fitz"]

    # for i in range(4):
    #     hero = LOL(name=HERO[i])
    #     session.add(hero)
    # session.commit()
    # heroes = session.query(LOL).all()
    # heroes = session.query(LOL.name, LOL.id).first()
    # heroes = session.query(func.count(LOL.id))

    # 条件查询 直接打印session.query(LOL).filter(LOL.id==1)结果为ORM底层转换的SQL语句 即在filter方法后不加任何方法之间返回
    # equals
    heroes = session.query(LOL).filter(LOL.id == 1).all()
    # not equals
    heroes = session.query(LOL).filter(LOL.id != 2).all()
    # heroes = session.query(LOL).filter(LOL.id == 2).all()
    # like
    heroes = session.query(LOL).filter(LOL.name.like("%aw%")).all()
    # in
    heroes = session.query(LOL).filter(LOL.name.in_(["Jiawen IV", "Rui Wen", "Fitz"])).all()
    # not in
    heroes = session.query(LOL).filter(LOL.name.notin_(["Jiawen IV", "Rui Wen", "Fitz"])).all()
    # not in  ~取反
    heroes = session.query(LOL).filter(~LOL.name.in_(["Jiawen IV", "Rui Wen", "Fitz"])).all()
    # is null is_
    heroes = session.query(LOL).filter(LOL.hp.is_(None)).all()
    # is not null
    heroes = session.query(LOL).filter(LOL.hp != None).all()
    # and
    heroes = session.query(LOL).filter(LOL.hp == None, LOL.id == 2).all()
    # and and_
    heroes = session.query(LOL).filter(and_(LOL.hp == None, LOL.id == 2)).all()
    # and 多次filter
    heroes = session.query(LOL).filter(LOL.hp == None).filter(LOL.id == 2).all()
    # or or_
    heroes = session.query(LOL).filter(or_(LOL.hp == 1000, LOL.name == "Rui Wen")).all()

    print(heroes)
    # for h in heroes:
    #     print(h)
