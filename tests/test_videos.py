import json

EXPECTED_KEYS = ['title', 'video_id', 'description', 'timestamp_publish', 'thumbnail_url']


class TestVideos(object):

    def test_get_videos(self, client, video):
        """Verify getting all videos. """
        video.add(video)
        request = client.get('/api/v1/videos.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        data = dict.get('data')
        assert len(data) == 1
        video = data[0]
        assert video.get('type') == 'video'
        attributes = video.get('attributes')
        assert attributes.get('title') == 'Expand Social Security'
        assert attributes.get('timestamp_publish') == '2016-01-13T19:08:43+00:00'
        assert list(attributes.keys()).sort() == EXPECTED_KEYS.sort()

    def test_get_single_video(self, client, video):
        """Verify getting a video item by ID."""
        video.add(video)
        request = client.get('/api/v1/videos/1.json')
        assert request.status_code == 200
        dict = json.loads(request.data.decode('utf-8'))
        video = dict.get('data')
        assert video.get('type') == 'video'
        attributes = video.get('attributes')
        assert attributes.get('title') == 'Expand Social Security'
        assert attributes.get('timestamp_publish') == '2016-01-13T19:08:43+00:00'
        assert list(attributes.keys()).sort() == EXPECTED_KEYS.sort()

    def test_get_nonexistent_video(self, client, video):
        """Verify trying to get a video item by ID that doesn't exist returns a 404."""
        video.add(video)
        request = client.get('/api/v1/videos/99.json')
        assert request.status_code == 404
