# -*- coding: utf-8 -*-#

# Name:         manage.py
# Description:  
# Author:       Mark
# Date:         2019\8\15 0015 11:07
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from app import app
# 需要把映射到数据库宗的模型导入manage.py文件中
from models import User


manager = Manager(app)
# 绑定app和db到flask_migrate
Migrate(app, db)
# 添加Migrate的所有子命令到db下
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()



