import os


class BaseConfig(object):
    """Base configuration."""
    HOST = "0.0.0.0"
    SECRET_KEY = 'feel the bern'
    DEBUG = False
    PORT = 5000
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    HOST = "127.0.0.1"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # Create in-memory db
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_ECHO = False  # Toggle to see db statements on error


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER='bernie',
        DB_PASS='sanders',
        DB_ADDR='sharkweek',
        DB_NAME='localhost'
    )
