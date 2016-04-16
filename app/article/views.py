from flask import Blueprint
from app.article.models import Article, ArticleSchema
from flask_restful import Api, Resource

article = Blueprint('article', __name__)
schema = ArticleSchema(
    strict=True,
    only=('title', 'body_markdown', 'excerpt', 'timestamp_publish', 'url', 'image_url', 'id')
)
api = Api(article)


class GetArticles(Resource):
    def get(self):
        # We only want Articles that are of article_type PressRelease OR DemocracyDaily
        article_query = Article.query.filter(Article.article_type.in_(['PressRelease', 'DemocracyDaily'])).all()
        results = schema.dump(article_query, many=True).data
        return results


class GetArticle(Resource):
    def get(self, id):
        article_query = Article.query.get_or_404(id)
        result = schema.dump(article_query).data
        return result


api.add_resource(GetArticles, '/api/v1/articles.json')
api.add_resource(GetArticle, '/api/v1/articles/<int:id>.json')
