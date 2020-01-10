from flask import Flask, jsonify,render_template,url_for
import qiniu
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/uptoken/')
def uptoken():
    access_key = '_MZMe1XwdcsqFnhpoqd2OtUC_VVaUr4ku6W1TIur'
    secret_key = 'QWfV-5wpbO6Of-f7JQ0R2K0phljk79Qd7KumSviJ'
    q = qiniu.Auth(access_key, secret_key)
    bucket = 'starspace'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})

if __name__ == '__main__':
    app.run(debug=True)
