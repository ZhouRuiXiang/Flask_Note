# -*- coding: utf-8 -*-#

# Name:         models.py
# Description:  
# Author:       Mark
# Date:         2019\8\14 0014 17:09
from exts import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Enum("男", "女", "保密"))


class Article(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship("User", backref=db.backref("my_articles"))
