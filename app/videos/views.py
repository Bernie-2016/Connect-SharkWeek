from flask import Blueprint, request, jsonify, make_response
from app.videos.models import Videos, VideosSchema
from flask_restful import Api, Resource
from app.basemodels import db
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

videos = Blueprint('videos', __name__)
# http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
# https://github.com/marshmallow-code/marshmallow-jsonapi
schema = VideosSchema(strict=True)
api = Api(videos)


class CreateListVideos(Resource):
    """
    http://jsonapi.org/format/#fetching
    A server MUST respond to a successful request to fetch an
    individual resource or resource collection with a 200 OK response.
    A server MUST respond with 404 Not Found when processing a request
    to fetch a single resource that does not exist, except when the request
    warrants a 200 OK response with null as the primary data (as described above)
    a self link as part of the top-level links object
    """
    def get(self):
        videos_query = Videos.query.all()
        results = schema.dump(videos_query, many=True).data
        return results

    """http://jsonapi.org/format/#crud
    A resource can be created by sending a POST request
    to a URL that represents a collection of articles.
    The request MUST include a single resource object as primary data.
    The resource object MUST contain at least a type member.
    If a POST request did not include a Client-Generated ID and the requested resource
    has been created successfully, the server MUST return a 201 Created status code
    """
    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            video = Videos(
                request_dict['status'],
                request_dict['video_id'],
                request_dict['url'],
                request_dict['site'],
                request_dict['title'],
                request_dict['description'],
                request_dict['thumbnail_url'],
                request_dict.get('timestamp_creation'),
                request_dict.get('timestamp_publish'),
                request_dict['description_snippet'],
            )
            video.add(video)
            query = Videos.query.get(video.id)
            results = schema.dump(query).data
            return results, 201

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp


class GetUpdateDeleteVideo(Resource):
    """http://jsonapi.org/format/#fetching
    A server MUST respond to a successful request to fetch
    an individual resource or resource collection with a 200 OK response.
    A server MUST respond with 404 Not Found when processing
    a request to fetch a single resource that does not exist,
    except when the request warrants a 200 OK response with null
    as the primary data (as described above)
    a self link as part of the top-level links object
    """
    def get(self, id):
        video_query = Videos.query.get_or_404(id)
        result = schema.dump(video_query).data
        return result

    """http://jsonapi.org/format/#crud-updating"""
    def patch(self, id):
        video = Videos.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
                setattr(video, key, value)

            video.update()
            return self.get(id)

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 401
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

    # http://jsonapi.org/format/#crud-deleting
    # A server MUST return a 204 No Content status code if a deletion request
    # is successful and no content is returned.
    def delete(self, id):
        video = Videos.query.get_or_404(id)
        try:
            video.delete(video)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp


api.add_resource(CreateListVideos, '/api/v1/videos.json')
api.add_resource(GetUpdateDeleteVideo, '/api/v1/videos/<int:id>.json')
