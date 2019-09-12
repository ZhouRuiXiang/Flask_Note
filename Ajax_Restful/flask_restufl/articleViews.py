from flask import Blueprint, render_template, Response, make_response
from flask_restful import Api, Resource, fields, marshal_with
from models import Article

article_bp = Blueprint('article', __name__, url_prefix='/article')
api = Api(article_bp)

@api.representation('text/html')
def output_html(data, code, headers):
    # print(data)
    print(code)
    print(headers)
    resp = make_response(data)
    # 必须放回Response对象
    return resp

class ArticleView(Resource):

    resource_fields = {
        # attribute="title"相当于将展示给前端接口换个名字
        "article_title": fields.String(attribute="title"),
        "article_content": fields.String(attribute="content"),
        "article_author": fields.Nested({
            "username": fields.String,
            "email": fields.String
        }, attribute="author"),
        "tags": fields.List(fields.Nested({
            "id": fields.Integer,
            "name": fields.String
        })),
        # Article表中没有该字段,所以这里可以设置一个default
        # 阅读量类似的数据一般没必要保存在数据库，所有可以从其他地方获取这个值
        "read_count": fields.Integer(default=80)
    }

    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article


api.add_resource(ArticleView, '/<article_id>/', endpoint='article')


class ListView(Resource):
    def get(self):
        return render_template('list.html')


api.add_resource(ListView, '/list/', endpoint='list')



