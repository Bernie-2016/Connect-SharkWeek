from marshmallow_jsonapi import Schema, fields
from app.basemodels import db, CRUD_MixIn


class Video(db.Model, CRUD_MixIn):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, nullable=False)
    video_id = db.Column(db.Text, nullable=False)
    timestamp_creation = db.Column(db.DateTime, nullable=False)
    timestamp_publish = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.Text, nullable=False)
    site = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    thumbnail_url = db.Column(db.Text, nullable=False)
    description_snippet = db.Column(db.Text, nullable=False)

    def __init__(self, status, video_id, url, site, title, description, thumbnail_url,
                 timestamp_creation, timestamp_publish, description_snippet, ):

        self.status = status
        self.video_id = video_id
        self.url = url
        self.site = site
        self.title = title
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.timestamp_creation = timestamp_creation
        self.timestamp_publish = timestamp_publish
        self.description_snippet = description_snippet


class VideoSchema(Schema):

    # id = fields.Integer(dump_only=True)
    id = fields.UUID(dump_only=True)

    status = fields.Integer(required=True)
    video_id = fields.String()
    timestamp_publish = fields.DateTime("%Y-%m-%dT%H:%M:%S+00:00")
    url = fields.Url()
    site = fields.String()
    title = fields.String()
    description = fields.String()
    thumbnail_url = fields.Url()
    description_snippet = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/videos/"
        else:
            self_link = "/videos/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'video'
