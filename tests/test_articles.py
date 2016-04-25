import json

from . import EXPECTED_ARTICLE_KEYS


class TestArticles(object):

    def test_get_single_article(self, client, dd_article):
        """Verify getting an article by ID."""
        dd_article.add(dd_article)
        request = client.get('/articles/1')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        article = dict.get('data')
        assert article.get('type') == 'article'
        attributes = article.get('attributes')
        assert attributes.get('title') == 'I Endorse Bernie Sanders for President'
        assert list(attributes.keys()).sort() == EXPECTED_ARTICLE_KEYS.sort()

    def test_get_nonexistent_article(self, client, dd_article):
        """Verify trying to get an article by ID that doesn't exist returns a 404."""
        dd_article.add(dd_article)
        request = client.get('/articles/99')
        assert request.status_code == 404
