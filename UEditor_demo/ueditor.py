# -*- coding:utf-8 -*- ,Author: XingChen
import os
import sys
import string
from flask import (
    Blueprint,
    current_app as app,
    request,
    url_for,
    jsonify,
    send_from_directory
)
import time
import random
import hashlib
import json
import re
from urllib import parse
import base64
# 更改工作目录。这么做的目的是
# 七牛的sdk在设置缓存路径的时候默认 会设置到C:/Windows/System32下面
# 会造成没有权限创建

os.chdir(os.path.dirname(__file__))
try:
    import qiniu
except:
    pass
from io import BytesIO
bp = Blueprint('ueditor', __name__, url_prefix='/ueditor')

UEDITOR_UPLOAD_PATH = ""
UEDITOR_UPLOAD_TO_QINIU = False
UEDITOR_QINIU_ACCESS_KEY = ""
UEDITOR_QINIU_SECRET_KEY = ""
UEDITOR_QINIU_BUCKET_NAME = ""
UEDITOR_QINIU_DOMAIN = ""

@bp.before_app_first_request
def before_first_request():
    global UEDITOR_UPLOAD_PATH
    global UEDITOR_UPLOAD_TO_QINIU
    global UEDITOR_QINIU_ACCESS_KEY
    global UEDITOR_QINIU_SECRET_KEY
    global UEDITOR_QINIU_BUCKET_NAME
    global UEDITOR_QINIU_DOMAIN
    UEDITOR_UPLOAD_PATH = app.config.get('UEDITOR_UPLOAD_PATH')
    if UEDITOR_UPLOAD_PATH and not os.path.exists(UEDITOR_UPLOAD_PATH):
        os.mkdir(UEDITOR_UPLOAD_PATH)
    UEDITOR_UPLOAD_TO_QINIU = app.config.get('UEDITOR_UPLOAD_TO_QINIU')
    if UEDITOR_UPLOAD_TO_QINIU:
        try:
            # UEDITOR_QINIU_ACCESS_KEY = app.confg['UEDITOR_QINIU_ACCESS_KEY']
            UEDITOR_QINIU_ACCESS_KEY = app.config.get('UEDITOR_QINIU_ACCESS_KEY')
            UEDITOR_QINIU_SECRET_KEY = app.config.get('UEDITOR_QINIU_SECRET_KEY')
            UEDITOR_QINIU_BUCKET_NAME = app.config.get('UEDITOR_QINIU_BUCKET_NAME')
            UEDITOR_QINIU_DOMAIN = app.config.get('UEDITOR_QINIU_DOMAIN')
        except Exception as e:
            option = e.args[0]
            raise RuntimeError('请在app.config中配置%s' %option)

def _random_filename(rawfilename):
    letters = string.ascii_letters
    random_filename = str(time.time()) + "".join(random.sample(letters, 5))
    filename = hashlib.md5(random_filename.encode('utf-8')).hexdigest()
    subffix = os.path.splitext(rawfilename)[-1]
    return filename + subffix


@bp.route('/upload/', methods=['GET', 'POST'])
def upload():
    action = request.args.get('action')
    result = {}
    if action == 'config':
        config_path = os.path.join(bp.static_folder or app.static_folder, 'ueditor', 'config.json')
        with open(config_path, 'r', encoding='utf-8')as fp:
            result = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))

    elif action in {'uploadimage', 'uploadvideo', 'uploadfile'}:
        image = request.files.get('upfile')
        filename = image.filename
        save_filename = _random_filename(filename)
        result = {
            'state': '',
            'url': '',
            'title': '',
            'original': ''
        }
        if UEDITOR_UPLOAD_TO_QINIU:
            if not sys.modules.get('qiniu'):
                raise RuntimeError('没有导入qiniu模块')
            q = qiniu.Auth(UEDITOR_QINIU_ACCESS_KEY, UEDITOR_QINIU_SECRET_KEY)
            token = q.upload_token(UEDITOR_QINIU_BUCKET_NAME)
            buffer = BytesIO()
            image.save(buffer)
            buffer.seek(0)
            ret, info = qiniu.put_data(token, save_filename, buffer.read())
            if info.ok:
                result['state'] = 'SUCCESS'
                result['url'] = parse.urljoin(UEDITOR_QINIU_DOMAIN, ret['key'])
                result['title'] = ret['key']
                result['original'] = ret['key']
        else:
            image.save(os.path.join(UEDITOR_UPLOAD_PATH, save_filename))
            result['state'] = 'SUCCESS'
            result['url'] = url_for('ueditor.files', filename=save_filename)
            result['title'] = save_filename
            result['original'] = image.filename
    elif action == 'uploadscrawl':
        base64data = request.form.get('upfile')
        img = base64.b64decode(base64data)
        filename = _random_filename('xx.png')
        filepath = os.path.join(UEDITOR_UPLOAD_PATH, filename)
        with open(filepath, 'wb')as fp:
            fp.write(img)
        result ={
            'state': 'SUCCESS',
            'url': url_for('files', filename=filename),
            'title': filename,
            'original':filename
        }
    return jsonify(result)


@bp.route('/files/<filename>/')
def files(filename):
    return send_from_directory(UEDITOR_UPLOAD_PATH, filename)
