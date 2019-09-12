# -*- coding: utf-8 -*-#
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/steal/')
def steal():
    return render_template('steal.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
