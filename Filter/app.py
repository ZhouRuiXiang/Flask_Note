from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def hello_world():
    context = {
        'str': 'abc',
        'time':datetime(2020,2,11,13,0,59,)
    }
    # return render_template('index.html', **context)
    return render_template('index.html', **context)


@app.template_filter()
def reverse(value):
    print(value)
    temp = list(value)
    temp.reverse()
    return ''.join(temp)


@app.template_filter()
def handle_time(time):
    """
        如果timestamp < 60s : 返回: 刚刚
        如果60s <= timestamp < 60*60s : 返回: n 分钟前 # n = timestamp // 60
        如果60*60s <= timestamp < 60*60*24s : 返回: n 小时前 # n = timestamp // （60*60）
        如果60*60*24s <= timestamp < 60*60*24*30s : 返回: n 天前 # n = timestamp // （60*60*24）
        如果60*60*24*30s <= timestamp < 60*60*24*30*12s : 返回: n个月 前 # n = timestamp // （60*60*24*30）
    """
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif 60 <= timestamp < 60 * 60:
            minutes = timestamp // 60
            return '%s分钟前' % int(minutes)
        elif 60 * 60 <= timestamp < 60 * 60 * 24:
            hours = timestamp // (60 * 60)
            return '%s小时前' % int(hours)
        elif 60 * 60 * 24 <= timestamp < 60 * 60 * 24 * 30:
            days = timestamp // (60 * 60 * 24)
            return '%s天前' % int(days)
        elif 60 * 60 * 24 * 30 <= timestamp < 60 * 60 * 24 * 30 * 12:
            months =timestamp // (60 * 60 * 24 *30)
            return '%s个月前' % int(months)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time
if __name__ == '__main__':
    app.run(debug=True)

