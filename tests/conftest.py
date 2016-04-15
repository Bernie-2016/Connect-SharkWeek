import datetime
import pytest

from app import create_app
from app.article.models import Article
from app.basemodels import db as _db
from app.config import TestingConfig
from app.news.models import News
from app.video.models import Video


def article(article_type):
    """
    'status'
    'article_id'
    'timestamp_creation'
    'timestamp_publish'
    'title'
    'article_type'
    'site'
    'lang'
    'excerpt'
    'article_category'
    'url'
    'image_url'
    'body'
    'body_markdown'
    """
    article = Article(
        1,
        "article_id",
        datetime.datetime.now(),
        datetime.datetime.strptime("2016-02-05T00:00:00", "%Y-%m-%dT%H:%M:%S"),
        "I Endorse Bernie Sanders for President",
        article_type,
        "site",
        "lang",
        "Thank you. It’s good to be back in New Hampshire...",
        "article_category",
        "https://berniesanders.com/i-endorse-bernie-sanders-for-president/",
        "https://berniesanders.com/wp-content/uploads/2016/02/NAACP-President-and-CEO-Benjamin-Jealous-404x250.png",
        "body",
        "#As prepared for delivery on February 5, 2016\nThank you. It’s good to be back in New Hampshire.",
    )
    return article


@pytest.fixture(scope="function")
def dd_article():
    return article(article_type="DemocracyDaily")


@pytest.fixture(scope="function")
def foo_article():
    return article(article_type="foo")


@pytest.fixture(scope="function")
def news():
    """
    status,
    news_id,
    timestamp_creation,
    timestamp_publish,
    title,
    news_type,
    site,
    lang,
    excerpt,
    news_category,
    url,
    image_url,
    body,
    body_markdown
    """
    news = News(
        1,
        "news_id",
        datetime.datetime.now(),
        datetime.datetime.strptime("2016-01-10T00:00:00", "%Y-%m-%dT%H:%M:%S"),
        "Get Connect Alerts on your iPhone with Movement App",
        "news_type",
        "site",
        "lang",
        "DES MOINES, Iowa – There was fresh evidence on Sunday that confirms Bernie Sanders...",
        "news_category",
        "https://berniesanders.com/press-release/electability-matters/",
        "https://berniesanders.com/wp-content/uploads/2016/02/image1-1.jpg",
        "body",
        "# DES MOINES, Iowa\nThere was fresh evidence on Sunday that confirms Bernie Sanders would be the most..."
    )
    return news


@pytest.fixture(scope="function")
def video():
    """
    status,
    video_id,
    url,
    site,
    title,
    description,
    thumbnail_url,
    timestamp_creation,
    timestamp_publish,
    description_snippet
    """
    video = Video(
        1,
        "c4e9yiuKAmY",
        "http://www.example.com/",
        "site",
        "Expand Social Security",
        "Get to da choppa",
        "http://www.example.com/image.png",
        datetime.datetime.now(),
        datetime.datetime.strptime("2016-01-13T19:08:43", "%Y-%m-%dT%H:%M:%S"),
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
