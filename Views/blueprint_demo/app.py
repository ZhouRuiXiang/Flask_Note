from flask import Flask, url_for, render_template
from blueprints.user import user_bp
from blueprints.cms import cms_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(cms_bp)

app.config.update({
    'DEBUG': True,
    'SERVER_NAME': 'baidu.com:5000'
})

@app.route('/')
def hello_world():
    print(url_for('user.my_profile'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
