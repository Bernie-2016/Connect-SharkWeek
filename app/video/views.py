from flask import Blueprint
from app.video.models import Video, VideoSchema
from flask_restful import Api, Resource

video = Blueprint('video', __name__)
schema = VideoSchema(
    strict=True,
    only=('title', 'video_id', 'description', 'timestamp_publish', 'thumbnail_url', 'id')
)
api = Api(video)


class GetVideos(Resource):
    def get(self):
        video_query = Video.query.all()
        results = schema.dump(video_query, many=True).data
        return results


class GetVideo(Resource):
    def get(self, id):
        video_query = Video.query.get_or_404(id)
        result = schema.dump(video_query).data
        return result


api.add_resource(GetVideos, '/api/v1/videos.json')
api.add_resource(GetVideo, '/api/v1/videos/<int:id>.json')
