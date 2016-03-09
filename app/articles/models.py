from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from app.basemodels import db, CRUD_MixIn


class Articles(db.Model, CRUD_MixIn):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, nullable=False)
    article_id = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    article_type = db.Column(db.Text, nullable=False)
    site = db.Column(db.Text, nullable=False)
    lang = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    article_category = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    body_markdown = db.Column(db.Text, nullable=False)

    def __init__(self, status, article_id, timestamp_creation, timestamp_publish, title, article_type,
                 site, lang, excerpt, article_category, url, image_url, body, body_markdown, ):

        self.status = status
        self.article_id = article_id
        self.timestamp_creation = timestamp_creation
        self.timestamp_publish = timestamp_publish
        self.title = title
        self.article_type = article_type
        self.site = site
        self.lang = lang
        self.excerpt = excerpt
        self.article_category = article_category
        self.url = url
        self.image_url = image_url
        self.body = body
        self.body_markdown = body_markdown


class ArticlesSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    # add validate=not_blank in required fields
    # id = fields.Integer(dump_only=True)
    id = fields.UUID(dump_only=True)

    status = fields.Integer(required=True)
    article_id = fields.String(validate=not_blank)
    title = fields.String(validate=not_blank)
    article_type = fields.String(validate=not_blank)
    site = fields.String(validate=not_blank)
    lang = fields.String(validate=not_blank)
    excerpt = fields.String(validate=not_blank)
    article_category = fields.String(validate=not_blank)
    url = fields.String(validate=not_blank)
    image_url = fields.String(validate=not_blank)
    body = fields.String(validate=not_blank)
    body_markdown = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/articles/"
        else:
            self_link = "/articles/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'articles'
