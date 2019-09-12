# -*- coding: utf-8 -*-#

# Name:         config.py
# Description:  
# Author:       Mark
# Date:         2019\8\22 0022 15:23
import os
USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "icbc"
DB_URI = "mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}".format(user=USERNAME, pwd=PASSWORD, host=HOST, port=PORT, db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
DEBUG = True

