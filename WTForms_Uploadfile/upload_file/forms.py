# -*- coding: utf-8 -*-#

# Name:         forms.py
# Description:  
# Author:       Mark
# Date:         2019\8\21 0021 13:52

from flask_wtf.file import FileAllowed, FileRequired
from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired


class UploadForm(Form):
    # 命名要和模板文件中name一致
    picture = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    description = StringField(validators=[InputRequired()])

