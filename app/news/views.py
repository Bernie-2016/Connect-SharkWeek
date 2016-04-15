from flask import Blueprint
from app.news.models import News, NewsSchema
from flask_restful import Api, Resource

news = Blueprint('news', __name__)
schema = NewsSchema(
    strict=True,
    only=('title', 'body_markdown', 'excerpt', 'timestamp_publish', 'url', 'image_url', 'id')
)
api = Api(news)


class GetNews(Resource):
    def get(self):
        news_query = News.query.all()
        results = schema.dump(news_query, many=True).data
        return results


class GetNewsItem(Resource):
    def get(self, id):
        news_query = News.query.get_or_404(id)
        result = schema.dump(news_query).data
        return result


api.add_resource(GetNews, '/api/v1/news.json')
api.add_resource(GetNewsItem, '/api/v1/news/<int:id>.json')
