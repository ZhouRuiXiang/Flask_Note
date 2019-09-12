# -*- coding: utf-8 -*-#

# Name:         manage.py
# Description:  
# Author:       Mark
# Date:         2019\8\22 0022 15:47
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from models import User
from app import app
from exts import db


manager = Manager(app=app)
Migrate(app, db=db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()