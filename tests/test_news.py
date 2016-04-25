import json

from . import EXPECTED_NEWS_KEYS


class TestNews(object):

    def test_get_single_news_item(self, client, news):
        """Verify getting a news item by ID."""
        news.add(news)
        request = client.get('/news/1')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        news = dict.get('data')
        assert news.get('type') == 'news'
        attributes = news.get('attributes')
        assert attributes.get('title') == 'Get Connect Alerts on your iPhone with Movement App'
        assert list(attributes.keys()).sort() == EXPECTED_NEWS_KEYS.sort()

    def test_get_nonexistent_news_item(self, client, news):
        """Verify trying to get a news item by ID that doesn't exist returns a 404."""
        news.add(news)
        request = client.get('/news/99')
        assert request.status_code == 404
