import os

# Settings for this Flask app
SHARK_HOST = os.environ.get('SHARK_HOST', '0.0.0.0')
SHARK_SECRET = os.environ.get('SHARK_SECRET', 'feel the bern')
SHARK_PORT = os.environ.get('SHARK_PORT', '5000')
SHARK_LOGGING_LEVEL = os.environ.get('SHARK_LOGGING_LEVEL', 'info')

# Settings for the backend DB
SHARK_DB_USER = os.environ.get('SHARK_DB_USER', 'bernie')
SHARK_DB_PASS = os.environ.get('SHARK_DB_PASS', 'sanders')
SHARK_DB_ADDR = os.environ.get('SHARK_DB_ADDR', 'sharkweek')
SHARK_DB_NAME = os.environ.get('SHARK_DB_NAME', 'localhost')


class BaseConfig(object):
    """Base configuration."""
    HOST = SHARK_HOST
    SECRET_KEY = SHARK_SECRET
    PORT = SHARK_PORT
    DEBUG = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    LOGGING_LEVEL = SHARK_LOGGING_LEVEL


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG = True
    DEBUG_TB_ENABLED = True


class HerokuDevConfig(DevelopmentConfig):
    """Deployment to heroku using local postgres instance."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # Create in-memory db
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_ECHO = False  # Toggle to see db statements on error


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=SHARK_DB_USER,
        DB_PASS=SHARK_DB_PASS,
        DB_ADDR=SHARK_DB_ADDR,
        DB_NAME=SHARK_DB_NAME
    )
