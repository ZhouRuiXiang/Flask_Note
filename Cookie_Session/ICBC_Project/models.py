# -*- coding: utf-8 -*-#

# Name:         models.py
# Description:  
# Author:       Mark
# Date:         2019\8\22 0022 15:36
from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    deposit = db.Column(db.Float, default=0)

    def __repr__(self):
        return "<User>%d %s %d" % (self.id, self.username, self.deposit)