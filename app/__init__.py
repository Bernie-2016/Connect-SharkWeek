from flask import Flask, jsonify, make_response
import os

from .basemodels import db
from app.config import ProductionConfig
from app.article.models import Article
from app.article.views import article
from app.article.views import schema as article_schema
from app.news.models import News
from app.news.views import news
from app.news.views import schema as news_schema
from app.video.models import Video
from app.video.views import video
from app.video.views import schema as video_schema


from logging import getLogger
LOGGER = getLogger(__name__)

# Limit for the total number of items returned.
SHARK_NEWSFEED_LIMIT = int(os.environ.get('SHARK_NEWSFEED_LIMIT', '30'))


def create_app(config_object=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    LOGGER.info('Starting up the application.')

    # DB setup
    db.init_app(app)

    # Blueprints
    app.register_blueprint(article)
    app.register_blueprint(news)
    app.register_blueprint(video)

    @app.route('/newsfeed', methods=['GET'])
    def get_newsfeed():
        newsfeed = {}
        newsfeed['links'] = {}

        # Because the newsfeed item can come from any of the 3 tables,
        # limit the query on each type to return at most SHARK_NEWSFEED_LIMIT items.
        article_query = Article.query.filter(Article.article_type.in_(['PressRelease', 'DemocracyDaily']))
        article_query = article_query.order_by(Article.timestamp_publish.desc())
        article_query = article_query.limit(SHARK_NEWSFEED_LIMIT).all()
        articles = article_schema.dump(article_query, many=True).data.get('data')

        news_query = News.query.order_by(News.timestamp_publish.desc())
        news_query = news_query.limit(SHARK_NEWSFEED_LIMIT).all()
        news = news_schema.dump(news_query, many=True).data.get('data')

        video_query = Video.query.order_by(Video.timestamp_publish.desc())
        video_query = video_query.limit(SHARK_NEWSFEED_LIMIT).all()
        videos = video_schema.dump(video_query, many=True).data.get('data')

        # Now after combining the items of all types into a single list, again
        # limit the total number of items that will be returned to the client.
        all_items = articles + news + videos
        all_items.sort(key=lambda _: _.get('attributes').get('timestamp_publish'), reverse=True)
        newsfeed['data'] = all_items[:SHARK_NEWSFEED_LIMIT]

        return jsonify(newsfeed)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app
