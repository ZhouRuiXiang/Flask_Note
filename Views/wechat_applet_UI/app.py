from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})

tv_data = [
    {
        "index":0,
        "title":"请回答1988 응답하라 1988",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2272563445.webp",
        "rating":"9.7"
    },
    {
        "index":1,
        "title":"大明王朝1566",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2444453078.webp",
        "rating":"9.7"
    },
    {
        "index":2,
        "title":"走向共和",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2328449064.webp",
        "rating":"9.7"
    },
    {
        "index":3,
        "title":"是，大臣 第一季 Yes Minister Season 1",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2187837239.webp",
        "rating":"9.7"
    },
    {
        "index":4,
        "title":"是，首相 第一季 Yes, Prime Minister Season 1",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2187836471.webp",
        "rating":"9.7"
    },
    {
        "index":5,
        "title":"老友记 第一季 Friends Season 1",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2186920269.webp",
        "rating":"9.6"
    },
    {
        "index":6,
        "title":"红楼梦",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2554030915.webp",
        "rating":"9.6"
    },
    {
        "index":7,
        "title":"白色巨塔 白い巨塔",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2199638898.webp",
        "rating":"9.6"
    },
    {
        "index":8,
        "title":"毛骗 终结篇",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2480805230.webp",
        "rating":"9.7"
    },
    {
        "index":9,
        "title":"武林外传",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2558313856.webp",
        "rating":"9.5"
    },
    {
        "index":10,
        "title":"西游记",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2265959269.webp",
        "rating":"9.5"
    },
    {
        "index":11,
        "title":"我们这一天 第一季 This Is Us Season 1",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2380810795.webp",
        "rating":"9.5"
    },
    {
        "index":12,
        "title":"兄弟连 Band of Brothers",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1714777727.webp",
        "rating":"9.5"
    },
    {
        "index":13,
        "title":"搞笑一家人 거침없이 하이킥!",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2187842414.webp",
        "rating":"9.5"
    },
    {
        "index":14,
        "title":"黑镜 第一季 Black Mirror Season 1",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1403875505.webp",
        "rating":"9.4"
    },
    {
        "index":15,
        "title":"非自然死亡 アンナチュラル",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2510604929.webp",
        "rating":"9.4"
    },
    {
        "index":16,
        "title":"权力的游戏 第一季 Game of Thrones Season 1",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p896064368.webp",
        "rating":"9.4"
    },
    {
        "index":17,
        "title":"生活大爆炸 第一季 The Big Bang Theory Season 1",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2553281898.webp",
        "rating":"9.4"
    },
    {
        "index":18,
        "title":"东京爱情故事 東京ラブストーリー",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2162780600.webp",
        "rating":"9.4"
    },
    {
        "index":19,
        "title":"摩登家庭 第一季 Modern Family Season 1",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p455073620.webp",
        "rating":"9.4"
    },
    {
        "index":20,
        "title":"机智牢房生活 슬기로운 감빵생활",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2506561091.webp",
        "rating":"9.4"
    },
    {
        "index":21,
        "title":"父母爱情",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2554351588.webp",
        "rating":"9.4"
    },
    {
        "index":22,
        "title":"成长的烦恼 第一季 Growing Pains Season 1",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2211723711.webp",
        "rating":"9.4"
    },
    {
        "index":23,
        "title":"憨豆先生 Mr. Bean",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2364077150.webp",
        "rating":"9.4"
    },
    {
        "index":24,
        "title":"毛骗 第二季",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1355804308.webp",
        "rating":"9.4"
    }
]
movie_data = [
    {
        "index":0,
        "title":"肖申克的救赎",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp",
        "rating":"9.6"
    },
    {
        "index":1,
        "title":"霸王别姬",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1488213971.webp",
        "rating":"9.6"
    },
    {
        "index":2,
        "title":"这个杀手不太冷",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p511118051.webp",
        "rating":"9.4"
    },
    {
        "index":3,
        "title":"阿甘正传",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2559011361.webp",
        "rating":"9.4"
    },
    {
        "index":4,
        "title":"美丽人生",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p510861873.webp",
        "rating":"9.5"
    },
    {
        "index":5,
        "title":"千与千寻",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.webp",
        "rating":"9.3"
    },
    {
        "index":6,
        "title":"泰坦尼克号",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p457760035.webp",
        "rating":"9.4"
    },
    {
        "index":7,
        "title":"辛德勒的名单",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2543441827.webp",
        "rating":"9.5"
    },
    {
        "index":8,
        "title":"盗梦空间",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p513344864.webp",
        "rating":"9.3"
    },
    {
        "index":9,
        "title":"忠犬八公的故事",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p524964016.webp",
        "rating":"9.3"
    },
    {
        "index":10,
        "title":"机器人总动员",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1461851991.webp",
        "rating":"9.3"
    },
    {
        "index":11,
        "title":"三傻大闹宝莱坞",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p579729551.webp",
        "rating":"9.2"
    },
    {
        "index":12,
        "title":"放牛班的春天",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1910824951.webp",
        "rating":"9.3"
    },
    {
        "index":13,
        "title":"海上钢琴师",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p511146807.webp",
        "rating":"9.2"
    },
    {
        "index":14,
        "title":"楚门的世界",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p479682972.webp",
        "rating":"9.2"
    },
    {
        "index":15,
        "title":"大话西游之大圣娶亲",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2455050536.webp",
        "rating":"9.2"
    },
    {
        "index":16,
        "title":"星际穿越",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2206088801.webp",
        "rating":"9.3"
    },
    {
        "index":17,
        "title":"龙猫",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2540924496.webp",
        "rating":"9.2"
    },
    {
        "index":18,
        "title":"教父",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p616779645.webp",
        "rating":"9.3"
    },
    {
        "index":19,
        "title":"熔炉",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1363250216.webp",
        "rating":"9.3"
    },
    {
        "index":20,
        "title":"无间道",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2233971046.webp",
        "rating":"9.2"
    },
    {
        "index":21,
        "title":"疯狂动物城",
        "thumbnail":"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2315672647.webp",
        "rating":"9.2"
    },
    {
        "index":22,
        "title":"当幸福来敲门",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1312700744.webp",
        "rating":"9.1"
    },
    {
        "index":23,
        "title":"怦然心动",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p663036666.webp",
        "rating":"9.0"
    },
    {
        "index":24,
        "title":"触不可及",
        "thumbnail":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1454261925.webp",
        "rating":"9.2"
    }
]



@app.route('/')
def hello_world():
    context = {
        'movie': movie_data,
        'tv':tv_data
    }
    return render_template('index.html', **context)

@app.route('/list/')
def item_list():
    category = request.args.get('category')
    if category == '1':
        items = movie_data
    else:
        items = tv_data
    return render_template('list.html', items=items)

if __name__ == '__main__':
    app.run()



