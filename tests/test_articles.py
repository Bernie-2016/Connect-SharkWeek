import json

EXPECTED_KEYS = ['title', 'body_markdown', 'excerpt', 'timestamp_publish', 'url', 'image_url']


class TestArticles(object):

    def test_article_type_filter(self, client, foo_article):
        """
        Verify that articles are filtered to include only those
        with an article_type of PressRelease OR DemocracyDaily.
        """
        foo_article.add(foo_article)
        request = client.get('/api/v1/articles.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 0

    def test_get_articles(self, client, dd_article):
        """Verify getting all articles."""
        dd_article.add(dd_article)
        request = client.get('/api/v1/articles.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 1
        article = data[0]
        assert article.get('type') == 'article'
        attributes = article.get('attributes')
        assert attributes.get('title') == 'I Endorse Bernie Sanders for President'
        assert list(attributes.keys()).sort() == EXPECTED_KEYS.sort()

    def test_get_single_article(self, client, dd_article):
        """Verify getting an article by ID."""
        dd_article.add(dd_article)
        request = client.get('/api/v1/articles/1.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        article = dict.get('data')
        assert article.get('type') == 'article'
        attributes = article.get('attributes')
        assert attributes.get('title') == 'I Endorse Bernie Sanders for President'
        assert list(attributes.keys()).sort() == EXPECTED_KEYS.sort()

    def test_get_nonexistent_article(self, client, dd_article):
        """Verify trying to get an article by ID that doesn't exist returns a 404."""
        dd_article.add(dd_article)
        request = client.get('/api/v1/articles/99.json')
        assert request.status_code == 404
