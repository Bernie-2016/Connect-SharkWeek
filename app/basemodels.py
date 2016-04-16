from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CRUD_MixIn():

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
