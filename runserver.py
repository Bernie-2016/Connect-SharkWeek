#!/usr/bin/env python
import os
from app import create_app

from logging import getLogger
LOGGER = getLogger(__name__)


CONFIG = os.environ.get('SHARK_APP_SETTINGS', 'app.config.DevelopmentConfig')

app = create_app(config_object=CONFIG)

if __name__ == '__main__':
    LOGGER.info("CONFIG: {}".format(CONFIG))
    LOGGER.info("HOST: {}".format(app.config['HOST']))
    LOGGER.info("PORT: {}".format(app.config['PORT']))

    app.run(host=app.config['HOST'],
            port=int(app.config['PORT']),
            debug=app.config['DEBUG'])
