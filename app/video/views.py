from flask import Blueprint
from app.video.models import Video, VideoSchema
from flask_restful import Api, Resource

video = Blueprint('video', __name__)
schema = VideoSchema(
    strict=True,
    only=('title', 'video_id', 'description', 'timestamp_publish', 'thumbnail_url', 'id')
)
api = Api(video)


class GetVideo(Resource):
    def get(self, id):
        video_query = Video.query.get_or_404(id)
        result = schema.dump(video_query).data
        return result

api.add_resource(GetVideo, '/videos/<int:id>')
