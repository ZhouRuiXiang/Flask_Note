# -*- coding: utf-8 -*-#

# Name:         forms.py
# Description:  
# Author:       Mark
# Date:         2019\8\22 0022 15:36
from wtforms import Form, StringField, FloatField
from wtforms.validators import Length, InputRequired, EqualTo, Email, NumberRange
from models import User


class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(min=3, max=20)])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[EqualTo("password")])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(min=6, max=10)])

    # def validate(self):
    #     result = super(LoginForm, self).validate()
    #     if not result:
    #         return False
    #     email = self.email.data
    #     password = self.password.data
    #     user = User.query.filter(User.email == email, User.password == password)
    #     if not user:
    #         self.email.errors.append("邮箱或密码不正确，请重新输入！")
    #         return False
    #     return True


class TransferForm(Form):
    email = StringField(validators=[Email()])
    amount = FloatField(validators=[NumberRange(1, 1000000)])