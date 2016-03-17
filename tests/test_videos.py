import json
from app.videos.models import Videos

data = """{
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


class TestVideos(object):

    def test_01_create(self, client):
        response = client.post('/api/v1/videos.json', data=data, content_type="application/json")
        assert response.status_code == 201

    def test_02_read_update(self, client, video):
        video.add(video)
        request = client.get('/api/v1/videos.json')
        dict = json.loads(request.data.decode('utf-8'))
        id = dict['data'][0]['id']
        response = client.patch('/api/v1/videos/{}.json'.format(id), data=data, content_type="application/json")
        assert response.status_code == 200

    def test_03_delete(self, client, video):
        video.add(video)
        videos = Videos.query.all()
        id = videos[0].id
        response = client.delete('/api/v1/videos/{}.json'.format(id))
        assert response.status_code == 204
