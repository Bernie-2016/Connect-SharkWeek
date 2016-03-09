from flask import Flask, jsonify, abort, make_response
from .basemodels import db
from app.config import ProductionConfig


def create_app(config_object=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # DB setup
    db.init_app(app)

    # Blueprints
    register_blueprints(app)

    @app.route('/')
    def index():
        return make_response(jsonify({'status': 'OK'}), 200)

    @app.route('/api/v1/newsfeed', methods=['GET'])
    def get_newsfeed():
        return jsonify({'newsfeed': []})

    @app.route('/api/v1/newsfeed/<int:newsfeed_id>', methods=['GET'])
    def get_news_item(newsfeed_id):
        news_item = []
        if len(news_item) == 0:
            abort(404)
        return jsonify({'news_item': news_item[0]})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app


def register_blueprints(app):
    from app.articles.views import articles
    app.register_blueprint(articles)
    from app.news.views import news
    app.register_blueprint(news)
    from app.videos.views import videos
    app.register_blueprint(videos)
    return None
