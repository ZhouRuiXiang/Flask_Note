# -*- coding: utf-8 -*-#

# Name:         ForeignKey_.py
# Description:  
# Author:       Mark
# Date:         2019\8\6 0006 17:35

from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

# DB_URI = "dialect+driver://username:password@host:port/database?charset=utf8"
USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "foreignkey"
DB_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class Hero(Base):
    # 表名
    __tablename__ = "hero"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    hp = Column(DECIMAL(5, 0))
    # my_skill = relationship("Skill", uselist=False)

    def __repr__(self):
        return "<Hero>name:%s hp:%d" % (self.name, self.hp)


class Skill(Base):
    # 表名
    __tablename__ = "skill"
    id = Column(Integer, autoincrement=True, primary_key=True)
    passive = Column(String(50), nullable=False)
    Q_ = Column(String(50), nullable=False)
    W_ = Column(String(50), nullable=False)
    E_ = Column(String(50), nullable=False)
    R_ = Column(String(50), nullable=False)
    Hid = Column(Integer, ForeignKey("hero.id", ondelete="CASCADE", ))
    owner = relationship("Hero", backref=backref("my_skill", uselist=False))

    def __repr__(self):
        return "<Skill>passive:{} Q:{} W:{} E:{} R:{}".format(self.passive, self.Q_, self.W_, self.E_, self.R_)


Base.metadata.drop_all()
Base.metadata.create_all()

heroes = [
    Hero(name="亚索", hp=609),
    Hero(name="菲兹", hp=570)
]
skills = [
    Skill(passive="浪客之道", Q_="斩钢闪", W_="风之障壁", E_="踏前斩", R_="狂风绝息斩", Hid=1),
    Skill(passive="伶俐斗士", Q_="淘气打击", W_="海石三叉戟", E_="古灵/精怪", R_="巨鲨强袭", Hid=2)

]

session.add_all(heroes)
session.add_all(skills)
print(heroes[0], skills[0])
print(heroes[1], skills[1])

hero1 = session.query(Hero).first()
hero2 = session.query(Hero).filter(Hero.id == 2).first()
print(type(hero1))
print(type(hero2))
# session.delete(hero1)
# session.delete(hero2)
session.commit()

# hero1 = session.query(Hero).first()
# skill1 = session.query(Skill).first()
# print(hero1.skill)
# print(skill1.hero)
# skill_1 = session.query(Skill).first()

# hero = Hero(name="菲兹", hp=570)
# skill = Skill(passive="伶俐斗士",  Q_="淘气打击", W_="海石三叉戟", E_="古灵/精怪", R_="巨鲨强袭")
# hero.my_skill.append(skill)
# session.add(hero)
# session.commit()
# print(type(skill))
# hero.my_skill = skill
# session.add(hero)
# session.commit()
# skill.owner = hero
# session.add(skill)
# session.commit()

