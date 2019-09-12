# -*- coding: utf-8 -*-#

# Name:         manage.py
# Description:  
# Author:       Mark
# Date:         2019\8\14 0014 15:42

from flask_script import Manager
from app import db, app, User
from db_manager import db_manager

manager = Manager(app)
manager.add_command('db', db_manager)


@manager.command
def greet():
    print("Hello World!")


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def add_user(username, password):
    db.session.add(User(username=username, password=password))
    db.session.commit()


if __name__ == '__main__':
    manager.run()

