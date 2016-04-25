import json
from . import EXPECTED_NEWS_KEYS, EXPECTED_ARTICLE_KEYS, EXPECTED_VIDEO_KEYS


class TestNewsfeed(object):

    def test_article_type_filter(self, client, foo_article):
        """
        Verify that articles are filtered to include only those
        with an article_type of PressRelease OR DemocracyDaily.
        """
        foo_article.add(foo_article)
        request = client.get('/newsfeed')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 0

    def test_get_articles(self, client, dd_article):
        """Verify getting all articles."""
        dd_article.add(dd_article)
        request = client.get('/newsfeed')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 1
        article = data[0]
        assert article.get('type') == 'article'
        attributes = article.get('attributes')
        assert attributes.get('title') == 'I Endorse Bernie Sanders for President'
        assert list(attributes.keys()).sort() == EXPECTED_ARTICLE_KEYS.sort()

    def test_get_news(self, client, news):
        """Verify getting all news items. """
        news.add(news)
        request = client.get('/newsfeed')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 1
        news_item = data[0]
        assert news_item.get('type') == 'news'
        attributes = news_item.get('attributes')
        assert attributes.get('title') == 'Get Connect Alerts on your iPhone with Movement App'
        assert attributes.get('timestamp_publish') == '2016-01-10T00:00:00+00:00'
        assert list(attributes.keys()).sort() == EXPECTED_NEWS_KEYS.sort()

    def test_get_videos(self, client, video):
        """Verify getting all videos. """
        video.add(video)
        request = client.get('/newsfeed')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 1
        video = data[0]
        assert video.get('type') == 'video'
        attributes = video.get('attributes')
        assert attributes.get('title') == 'Expand Social Security'
        assert attributes.get('timestamp_publish') == '2016-01-13T19:08:43+00:00'
        assert list(attributes.keys()).sort() == EXPECTED_VIDEO_KEYS.sort()

    def test_get_all_types(self, client, video, news, dd_article):
        """Verify getting items of all three types together. """
        news.add(news)
        video.add(video)
        dd_article.add(dd_article)
        request = client.get('/newsfeed')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 3
        item_types = []
        for item in data:
            item_types.append(item.get('type'))
        expected_types = ['video', 'news', 'article']
        assert item_types.sort() == expected_types.sort()

    def test_sorting(self, client, video, news, dd_article):
        """Verify items are returned in the correct sort order. """
        news.add(news)
        video.add(video)
        dd_article.add(dd_article)
        request = client.get('/newsfeed')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 3
        assert data[0].get('type') == 'article'
        assert data[0].get('attributes').get('timestamp_publish') == '2016-02-05T00:00:00+00:00'
        assert data[1].get('type') == 'video'
        assert data[1].get('attributes').get('timestamp_publish') == '2016-01-13T19:08:43+00:00'
        assert data[2].get('type') == 'news'
        assert data[2].get('attributes').get('timestamp_publish') == '2016-01-10T00:00:00+00:00'
