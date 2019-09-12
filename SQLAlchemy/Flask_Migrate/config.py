# -*- coding: utf-8 -*-#

# Name:         config.py
# Description:  
# Author:       Mark
# Date:         2019\8\14 0014 17:07
USERNAME = "root"
PASSWORD = "286977"
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "flask_migrate"
DB_URI = "mysql+mysqlconnector://%s:%s@%s:%s/%s" % (USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True