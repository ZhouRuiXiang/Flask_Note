# -*- coding: utf-8 -*-#

# Name:         多对多关系.py
# Description:  
# Author:       Mark
# Date:         2019\8\7 0007 17:11


from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

# DB_URI = "dialect+driver://username:password@host:port/database?charset=utf8"
USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "lol"
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

# 1. 创建需要做多对多关系映射的两个模型
# 2. 创建一个中间表，一般是两个模型中的主键
# 3. 选择一个模型，定义一个relationship属性并传入secondary=中间表，连接三个表，


class Hero(Base):
    __tablename__ = "hero"
    __tablename__ = "hero"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    hp = Column(DECIMAL(5, 0))


hero_weapon = Table(
    "hero_weapon",
    Base.metadata,
    Column("hero_id", Integer, ForeignKey("hero.id"), primary_key=True),
    Column("weapon_id", Integer, ForeignKey("weapon.id"), primary_key=True)
)


class Weapon(Base):
    __tablename__ = "weapon"
    id = Column(Integer, autoincrement=True, primary_key=True)
    w_name = Column(String(50), nullable=False)
    w_price = Column(DECIMAL(5, 0))
    my_owners = relationship("Hero", backref="my_weapons", secondary=hero_weapon)


Base.metadata.drop_all()
Base.metadata.create_all()

if __name__ == '__main__':
    weapon_1 = Weapon(w_name="无尽之刃")
    weapon_2 = Weapon(w_name="饮血剑")
    hero_1 = Hero(name="亚索")
    hero_2 = Hero(name="库奇")
    hero_1.my_weapons.append(weapon_1)
    hero_1.my_weapons.append(weapon_2)

    hero_2.my_weapons.append(weapon_1)
    hero_2.my_weapons.append(weapon_2)
    session.add(hero_1)
    session.add(hero_2)
    session.commit()