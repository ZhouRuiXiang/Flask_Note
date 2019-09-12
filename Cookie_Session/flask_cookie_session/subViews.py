# -*- coding: utf-8 -*-#

# Name:         subViews.py
# Description:  
# Author:       Mark
# Date:         2019\8\21 0021 17:32
from flask import Blueprint, request

bp = Blueprint("sub", __name__, subdomain="sub")


@bp.route('/')
def index():
    username = request.cookies.get("username")
    return username or "没有获取到cookie"