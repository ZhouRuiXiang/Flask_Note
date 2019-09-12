# -*- coding: utf-8 -*-#

# Name:         config.py
# Description:  
# Author:       Mark
# Date:         2019\8\30 0030 13:55


USERNAME = "root"
PASSWORD = "286977"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "flask_restful_demo"

DB_URI = "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True


