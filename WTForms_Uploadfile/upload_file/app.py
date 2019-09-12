# -*- coding: utf-8 -*-#
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import os
from forms import *

app = Flask(__name__)

UPLOAD_SAVE = os.path.join(os.path.dirname(__file__), "images")
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload/', methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            # desc = request.form.get("description")
            desc = form.description.data
            # pic = request.files.get("picture")
            pic = form.picture.data
            # 对中文不太友好，若文件名为全中文，则符号'.'会消失
            # 栗子：捕获.png -> png
            # 利用secure_filename方法防止 /../../bashrc 防止传入恶意文件名 来替换系统文件
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(UPLOAD_SAVE, filename))
            print(desc)
            return "文件上传成功"
        else:
            print(form.errors)
            return "文件上传失败"

@app.route('/images/<filename>/')
def get_image(filename):
    return send_from_directory(UPLOAD_SAVE, filename)

if __name__ == '__main__':
    app.run()
