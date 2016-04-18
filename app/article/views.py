from flask import Blueprint
from app.article.models import Article, ArticleSchema
from flask_restful import Api, Resource

article = Blueprint('article', __name__)
schema = ArticleSchema(
    strict=True,
    only=('title', 'body_markdown', 'excerpt', 'timestamp_publish', 'url', 'image_url', 'id')
)
api = Api(article)


class GetArticle(Resource):
    def get(self, id):
        article_query = Article.query.get_or_404(id)
        result = schema.dump(article_query).data
        return result

api.add_resource(GetArticle, '/articles/<int:id>')
