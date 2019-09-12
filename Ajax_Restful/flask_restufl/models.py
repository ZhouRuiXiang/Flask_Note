# -*- coding: utf-8 -*-#

# Name:         models.py
# Description:  
# Author:       Mark
# Date:         2019\8\30 0030 14:07
from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


article_tag_table = db.Table('article_tag',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref='my_articles')
    tags = db.relationship('Tag', secondary=article_tag_table, backref='articles')




