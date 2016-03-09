import unittest
import json

from tests.base import BaseTestCase

add_data = """{
  "data": {
    "attributes":
    {"lang": "foo",
     "image_url": "http://www.example.com",
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

update_data = """{
  "data": {
    "attributes":
        {"lang": "foo",
         "image_url": "http://www.example.com",
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


class TestNews(BaseTestCase):

    def setUp(self):
        super(TestNews, self).setUp()

    def test_01_add(self):
        rv = self.client.post('/api/v1/news.json', data=add_data, content_type="application/json")
        assert rv.status_code == 201

    def test_02_read_update(self):
        rv = self.client.post('/api/v1/news.json', data=add_data, content_type="application/json")
        request = self.client.get('/api/v1/news.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        rv = self.client.patch('/api/v1/news/{}.json'.format(id), data=update_data, content_type="application/json")
        assert rv.status_code == 200

    def test_03_delete(self):
        rv = self.client.post('/api/v1/news.json', data=add_data, content_type="application/json")
        request = self.client.get('/api/v1/news.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        rv = self.client.delete('/api/v1/news/{}.json'.format(id))
        assert rv.status_code == 204

if __name__ == '__main__':
    unittest.main()
