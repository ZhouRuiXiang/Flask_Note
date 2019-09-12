from flask import Blueprint, render_template, url_for

user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder='test')


@user_bp.route('/profile/')
def my_profile():
    return render_template('test.html')

@user_bp.route('/settings/')
def my_settings():
    print(url_for('user.my_profile'))
    return '设置页面'
