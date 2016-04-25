from marshmallow_jsonapi import Schema, fields
from app.basemodels import db, CRUD_MixIn


class News(db.Model, CRUD_MixIn):
    uuid = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, nullable=False)
    news_id = db.Column(db.Text, nullable=False)
    timestamp_creation = db.Column(db.DateTime, nullable=False)
    timestamp_publish = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.Text, nullable=False)
    news_type = db.Column(db.Text, nullable=False)
    site = db.Column(db.Text, nullable=False)
    lang = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    news_category = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    body_markdown = db.Column(db.Text, nullable=False)

    def __init__(self, status, news_id, timestamp_creation, timestamp_publish, title, news_type,
                 site, lang, excerpt, news_category, url, image_url, body, body_markdown, ):

        self.status = status
        self.news_id = news_id
        self.timestamp_creation = timestamp_creation
        self.timestamp_publish = timestamp_publish
        self.title = title
        self.news_type = news_type
        self.site = site
        self.lang = lang
        self.excerpt = excerpt
        self.news_category = news_category
        self.url = url
        self.image_url = image_url
        self.body = body
        self.body_markdown = body_markdown


class NewsSchema(Schema):

    id = fields.UUID(dump_only=True, attribute='uuid')

    status = fields.Integer()
    news_id = fields.String()
    timestamp_publish = fields.DateTime("%Y-%m-%dT%H:%M:%S+00:00")
    title = fields.String()
    news_type = fields.String()
    site = fields.String()
    lang = fields.String()
    excerpt = fields.String()
    news_category = fields.String()
    url = fields.Url()
    image_url = fields.String()
    body = fields.String()
    body_markdown = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/news/"
        else:
            self_link = "/news/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'news'
