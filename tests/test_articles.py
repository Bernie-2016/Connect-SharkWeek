import unittest
import json

from tests.base import BaseTestCase

add_data = """{
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

update_data = """{
  "data": {
    "attributes":

        {"lang": "bar",
        "image_url": "bar",
        "url": "bar",
        "article_id": "bar",
        "article_type": "bar",
        "excerpt": "bar",
        "status": 35678,
        "title": "bar",
        "body": "bar",
        "site": "bar",
        "body_markdown": "bar",
        "article_category": "bar"},
        "type": "articles"
  }
}"""


class TestArticles(BaseTestCase):

    def setUp(self):
        super(TestArticles, self).setUp()

    def test_01_add(self):
        rv = self.client.post('/api/v1/articles.json', data=add_data, content_type="application/json")
        assert rv.status_code == 201

    def test_02_read_update(self):
        self.client.post('/api/v1/articles.json', data=add_data, content_type="application/json")
        request = self.client.get('/api/v1/articles.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        rv = self.client.patch('/api/v1/articles/{}.json'.format(id), data=update_data, content_type="application/json")
        assert rv.status_code == 200

    def test_03_delete(self):
        self.client.post('/api/v1/articles.json', data=add_data, content_type="application/json")
        request = self.client.get('/api/v1/articles.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        rv = self.client.delete('/api/v1/articles/{}.json'.format(id))
        assert rv.status_code == 204

if __name__ == '__main__':
    unittest.main()
