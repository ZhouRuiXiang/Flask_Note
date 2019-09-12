# -*- coding: utf-8 -*-#

# Name:         forms.py
# Description:  
# Author:       Mark
# Date:         2019\8\20 0020 15:10


from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo, ValidationError


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名必须为3至10个字符")])
    password = StringField(validators=[Length(min=6, max=10, message="用户名必须为6至10个字符")])
    repeat_password = StringField(validators=[Length(min=6, max=10, message="用户名必须为6至10个字符"), EqualTo("password", message="两次密码输入不一致")])


class LoginForm(Form):
    username = StringField(validators=[Length(min=3, max=10)])
    password = StringField(validators=[Length(min=6, max=10)])
    captcha = StringField(validators=[Length(min=4, max=4)])

    def validate_captcha(self, field):
        if field.data != "asdf":
            raise ValidationError("验证码错误！")


class SettingsForm(Form):
    username = StringField("用户名", validators=[Length(min=3, max=10)])
    password = StringField("密码", validators=[Length(min=6, max=10)])
