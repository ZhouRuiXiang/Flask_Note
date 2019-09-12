# -*- coding: utf-8 -*-#
from flask import Flask

import config
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)




@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/profile')
def profile():
    pass



if __name__ == '__main__':
    app.run()
