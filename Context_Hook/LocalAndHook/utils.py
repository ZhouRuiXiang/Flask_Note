# -*- coding: utf-8 -*-#

# Name:         utils.py
# Description:  
# Author:       Mark
# Date:         2019\8\27 0027 13:37
from flask import g


def log_a():
    print("%s做了a事情" % g.username)


def log_b():
    print("%s做了b事情" % g.username)