import unittest
import json

from tests.base import BaseTestCase

add_data = """{
  "data": {
    "attributes":
    {"site": "foo",
     "url": "http://www.example.com",
     "description": "foo",
     "thumbnail_url": "http://www.example.com",
     "status": 35678,
     "title": "foo",
     "description_snippet": "foo",
     "video_id": "foo"},
    "type": "videos"
  }
 }"""

update_data = """{
  "data": {
    "attributes":
        {"site": "foo",
         "url": "http://www.example.com",
         "description": "foo",
         "thumbnail_url": "http://www.example.com",
         "status": 35678,
         "title": "foo",
         "description_snippet": "foo",
         "video_id": "foo"},
    "type": "videos"
  }
 }"""


class TestVideos(BaseTestCase):

    def setUp(self):
        super(TestVideos, self).setUp()

    def test_01_add(self):
        rv = self.client.post('/api/v1/videos.json', data=add_data, content_type="application/json")
        assert rv.status_code == 201

    def test_02_read_update(self):
        rv = self.client.post('/api/v1/videos.json', data=add_data, content_type="application/json")
        request = self.client.get('/api/v1/videos.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        rv = self.client.patch('/api/v1/videos/{}.json'.format(id), data=update_data, content_type="application/json")
        assert rv.status_code == 200

    def test_03_delete(self):
        rv = self.client.post('/api/v1/videos.json', data=add_data, content_type="application/json")
        request = self.client.get('/api/v1/videos.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        rv = self.client.delete('/api/v1/videos/{}.json'.format(id))
        assert rv.status_code == 204

if __name__ == '__main__':
    unittest.main()
