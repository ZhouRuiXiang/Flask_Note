# -*- coding: utf-8 -*-#

# Name:         operating.py
# Description:  
# Author:       Mark
# Date:         2019\8\1 0001 15:02


# import SQLAlchemy_Demo.SQLAlchemy_mappings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  SQLAlchemy_Demo.SQLAlchemy_mappings import DB_URI
from  SQLAlchemy_Demo.SQLAlchemy_mappings import Person

# 连接数据库
engine = create_engine(DB_URI)
# 创建一个会话
Session = sessionmaker(bind=engine)
session = Session()

# 生成一条数据对象
data_single = Person(name="Mark", age=19, reigon="Hubei Wuhan")
session.add(data_single)
try:
    pass
    # 提交事务
    # session.commit()
except Exception as e:
    print(e)
# 关闭会话
session.close()

# 生成多条数据的对象

data_multi = [
    Person(name="张三", age=20, reigon="湖北武汉"),
    Person(name="李四", age=10, reigon="福建厦门"),
    Person(name="王五", age=20, reigon="北京"),
    Person(name="赵四", age=20, reigon="四川成都")
]
session.add_all(data_multi)
try:
    pass
    # session.commit()
except Exception as e:
    print(e)
session.close()

# 查询在Person类(person表)中id==1的行并删除
# session.query(Person).filter(Person.id==1).delete()

# filter条件过滤使用的是比较运算符，可以写多个条件，多个条件之间是与的关系
session.query(Person).filter(Person.id > 3, Person.age == 20).delete()
try:
    pass
    # session.commit()
except Exception as e:
    print(e)
session.close()

# 修改数据通过字典的方式
session.query(Person).filter(Person.id == 3).update({"name": "路飞", "reigon": "东海"})
session.query(Person).filter(Person.id == 4).update({"name": "索隆", "reigon": "东海"})
session.query(Person).filter(Person.id == 5).update({"name": "山治", "reigon": "北海"})
try:
    pass
    # session.commit()
except Exception as e:
    print(e)
session.close()

# 查询
# filter只支持多条件查询，filter_by支持组合查询
# rows = session.query(Person).filter(Person.reigon == "东海").all()
rows = session.query(Person).filter_by(name="路飞", age=10).all()

for row in rows:
    print(row.name, row.age, row.reigon)
try:
    # pass
    session.commit()
except Exception as e:
    print(e)
for row in rows:
    print(row.name, row.age, row.reigon)
session.close()