from flask import Flask, render_template, url_for, views
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', endpoint='index')
def index():
    return render_template('index.html', about='关于我们')


# @app.route('/list/')
# def my_list():
#     return render_template('posts/list.html')
#
# app.add_url_rule('/list/',endpoint='myList',view_func=my_list)

# app.test_request_context() 请求上下文
# with app.test_request_context():
#     print(url_for('myList'))


class ListView(views.View):
    """
    标准类视图必须继承自Flask包下的views文件下的View类
    """
    def dispatch_request(self):
        """
        必须要实现的方法
        :return:同视图函数的返回值一样
        """
        return '我是视图函数'
# endpoint: 这个/list/路径的名字
# as_view()类方法中指定的参数: 视图函数的名字
app.add_url_rule('/list/', endpoint='my_list', view_func=ListView.as_view('list'))
with app.test_request_context():
    # url_for()的第一个参数: 若endpoint不为None则必须使用指定值，否则应使用视图函数的名字
    print(url_for('my_list'))




@app.route('/login/<int:id>')
def my_login(id):
    context = {
        'username': 'Star',
        'age': '-21',
        'sex': 'male',
        'location': {
            'country': 'China',
            'province': 'HuBei',
            'city': 'WuHan'
        },
        'books': [
            {
                'number': 1,
                'name': '三国演义',
                'author': '罗贯中',
                'prize': '109'
            },
            {
                'number': 2,
                'name': '水浒传',
                'author': '施耐庵',
                'prize': '119'
            },
            {
                'number': 3,
                'name': '天龙八部',
                'author': '金庸',
                'prize': '129'
            },
        ],
        'hobbies': ['playing guitar', 'playing badminton', 'playing billiard'],
        'signature': None,
        'alert': '<script>alert("Hello Star")</script>',
        'article': '习近平到赤峰考察调研，传递着这些牵挂',
        'create_time': datetime(2019, 7, 16, 17, 51, 0, 0)
    }
    return render_template('login.html', **context)


@app.template_filter('strip')
def strip(value, char):
    value = value.strip(char)
    return value





@app.template_filter('time_interval')
def time_interval(time):
    '''
    发布时间距离现在的时间间隔
    1. 小于1分钟显示 刚刚
    2. 大于等于1分钟且小于1小时显示 xx分钟前
    3. 大于等于1小时且小于1天显示 xx小时前
    4. 大于等于1天且小于30天显示 xx天前
    5. 否则显示具体时间 例如 2019/7/16 12:00

    '''
    if isinstance(time, datetime):
        now = datetime.now()
        interval = (now - time).total_seconds()
        if interval < 60:
            return '刚刚'
        # elif interval >= 60 and interval < 60 * 60:
        elif 60 <= interval < 60*60:
            minutes = int(interval / 60)
            return '%d分钟前' % minutes
        # elif interval >= 60 * 60 and interval < 60 * 60 * 24:
        elif 60*60 <= interval < 60*60*24:
            hours = int(interval / (60*60))
            return '%d小时前' %hours
        # elif interval >= 60 * 60 * 24 and interval < 60 * 60 * 24 * 30:
        elif 60*60*24 <= interval < 60*60*24*30:
            days = int(interval / (60*60*24))
            return '%d天前' %days
        else:
            return time.strftime('%Y/%m/%d %H:%M')

    else:
        return time
if __name__ == '__main__':
    app.run(Debug=True)
