import datetime
import pytest

from app import create_app
from app.articles.models import Articles
from app.basemodels import db as _db
from app.config import TestingConfig
from app.news.models import News
from app.videos.models import Videos


@pytest.fixture(scope="function")
def article():
    article = Articles(
        1,
        "article_id",
        datetime.datetime.now(),
        datetime.datetime.now(),
        "title",
        "article_type",
        "site",
        "lang",
        "excerpt",
        "article_category",
        "http://www.example.com",
        "http://www.example.com/image.png",
        "body",
        "body_markdown",
    )
    return article


@pytest.fixture(scope="function")
def news():
    news = News(
        1,
        "news_id",
        datetime.datetime.now(),
        datetime.datetime.now(),
        "title",
        "news_type",
        "site",
        "lang",
        "excerpt",
        "news_category",
        "http://www.example.com/",
        "http://www.example.com/image.png",
        "body",
        "body_markdown"
    )
    return news


@pytest.fixture(scope="function")
def video():
    video = Videos(
        1,
        "video_id",
        "http://www.example.com/",
        "site",
        "title",
        "description",
        "http://www.example.com/image.png",
        datetime.datetime.now(),
        datetime.datetime.now(),
        "description_snippet"
    )
    return video


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app(TestingConfig)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def db(app, request):
    """Test method-wide test database."""
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def client(db, request):
    """Test method-wide test client."""
    app = db.app
    return app.test_client()
