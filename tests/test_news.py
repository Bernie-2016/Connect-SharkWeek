import json
from app.news.models import News

data = """{
  "data": {
    "attributes":
    {"lang": "foo",
     "image_url": "http://www.example.com/image.png",
     "url": "http://www.example.com",
     "excerpt": "foo",
     "news_category": "foo",
     "news_id": "foo",
     "status": 35678,
     "title": "foo",
     "body": "foo",
     "site": "foo",
     "news_type": "foo",
     "body_markdown": "foo"} ,
    "type": "news"
  }
 }"""


class TestNews(object):

    def test_01_create(self, client):
        response = client.post('/api/v1/news.json', data=data, content_type="application/json")
        assert response.status_code == 201

    def test_02_read_update(self, client, news):
        news.add(news)
        request = client.get('/api/v1/news.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        response = client.patch('/api/v1/news/{}.json'.format(id), data=data, content_type="application/json")
        assert response.status_code == 200

    def test_03_delete(self, client, news):
        news.add(news)
        newses = News.query.all()
        id = newses[0].id
        response = client.delete('/api/v1/news/{}.json'.format(id))
        assert response.status_code == 204
