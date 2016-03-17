import json
from app.articles.models import Articles

data = """{
  "data": {
    "attributes":
    {"lang": "foo",
    "image_url": "foo",
    "url": "foo",
    "article_id": "foo",
    "article_type": "foo",
    "excerpt": "foo",
    "status": 35678,
    "title": "foo",
    "body": "foo",
    "site": "foo",
    "body_markdown": "foo",
    "article_category": "foo"},
    "type": "articles"
  }
}"""


class TestArticles(object):

    def test_01_create(self, client):
        response = client.post('/api/v1/articles.json', data=data, content_type="application/json")
        assert response.status_code == 201

    def test_02_read_update(self, client, article):
        article.add(article)
        request = client.get('/api/v1/articles.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        response = client.patch('/api/v1/articles/{}.json'.format(id), data=data, content_type="application/json")
        assert response.status_code == 200

    def test_03_delete(self, client, article):
        article.add(article)
        articles = Articles.query.all()
        id = articles[0].id
        response = client.delete('/api/v1/articles/{}.json'.format(id))
        assert response.status_code == 204
