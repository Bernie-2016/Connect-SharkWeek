from flask.ext.testing import TestCase
from app import create_app
from app.basemodels import db
from app.config import TestingConfig


class BaseTestCase(TestCase):

    def create_app(self):
        return create_app(TestingConfig)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
