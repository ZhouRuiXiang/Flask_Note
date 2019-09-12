# -*- coding: utf-8 -*-#

# Name:         demo.py
# Description:  
# Author:       Mark
# Date:         2019\7\31 0031 14:06

# 连接数据库之前先要创建数据库
from sqlalchemy import create_engine

HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "first_sqlalchemy"
USERNAME = "root"
PASSWORD = "286977"

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8"\
            .format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,database=DATABASE)

# 连接数据库
engine = create_engine(DB_URI,echo=True)

# 判断是否连接成功
# conn = engine.connect()
# result = conn.execute("select 1")
# print(result.fetchone())

# 使用with语句连接数据库，若发生异常会被捕获
with engine.connect() as conn:
    # 若存在users表，先删除
    conn.execute("drop table if exists users")
    # 创建users表
    conn.execute("create table users(id int primary KEY  auto_increment,"
                 "name varchar(25))")
    # 插入三条数据
    conn.execute("insert into users (name ) values ('Elijah')")
    conn.execute("insert into users (name ) values ('Rebeka')")
    conn.execute("insert into users (name ) values ('Klaus')")

    # 查询
    result = conn.execute("select * from users")
    for row in result:
        print(row)


