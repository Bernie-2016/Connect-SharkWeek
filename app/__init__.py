from flask import Flask, jsonify, make_response

from .basemodels import db
from app.config import ProductionConfig
from app.article.views import article
from app.news.views import news
from app.video.views import video

from logging import getLogger
LOGGER = getLogger(__name__)


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

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app
