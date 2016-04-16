import json

EXPECTED_KEYS = ['title', 'body_markdown', 'excerpt', 'timestamp_publish', 'url', 'image_url']


class TestNews(object):

    def test_get_news(self, client, news):
        """Verify getting all news items. """
        news.add(news)
        request = client.get('/api/v1/news.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 1
        news_item = data[0]
        assert news_item.get('type') == 'news'
        attributes = news_item.get('attributes')
        assert attributes.get('title') == 'Get Connect Alerts on your iPhone with Movement App'
        assert attributes.get('timestamp_publish') == '2016-01-10T00:00:00+00:00'
        assert list(attributes.keys()).sort() == EXPECTED_KEYS.sort()

    def test_get_single_news_item(self, client, news):
        """Verify getting a news item by ID."""
        news.add(news)
        request = client.get('/api/v1/news/1.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        news = dict.get('data')
        assert news.get('type') == 'news'
        attributes = news.get('attributes')
        assert attributes.get('title') == 'Get Connect Alerts on your iPhone with Movement App'
        assert list(attributes.keys()).sort() == EXPECTED_KEYS.sort()

    def test_get_nonexistent_news_item(self, client, news):
        """Verify trying to get a news item by ID that doesn't exist returns a 404."""
        news.add(news)
        request = client.get('/api/v1/news/99.json')
        assert request.status_code == 404
