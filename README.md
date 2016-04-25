# Connect-SharkWeek
Public API for [Sharknado](https://github.com/Bernie-2016/Connect-Sharknado) using the
[JSON API 1.0 Spec](http://jsonapi.org/)
[Newsfeed spec](https://github.com/Bernie-2016/Connect-SharkWeek/issues/3)

## Development
Make sure you have the following installed:
* postgresql 9.4
* python 3.5.1

We recommended that you use
[`virtualenv`](https://virtualenv.pypa.io/en/latest/),
[`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org), or a
similar tool to keep your development environment isolated from the
rest of your system.

Install all requirements:
```bash
make develop
```

Test code quality:
```bash
make quality
```

Run tests:
```bash
make test
```

Here are the commands for setting up the DB:
```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

To start the app in local development mode:
```bash
make run
```

## Application Configuration
Application configuration is handled by the OS environment variable SHARK_APP_SETTINGS.
Set this to one of the classes in app/config.py. For example:

For local development mode (this is the default):
SHARK_APP_SETTINGS=app.config.DevelopmentConfig

For production mode:
SHARK_APP_SETTINGS=app.config.ProductionConfig

Use the following environment variables to override the defaults in app/config.py.

Settings for this Flask app:
* SHARK_HOST
* SHARK_SECRET
* SHARK_PORT
* SHARK_NEWSFEED_LIMIT (default = 30)
* SHARK_LOGGING_LEVEL (default = info)

Settings for the backend DB:
* SHARK_DB_USER
* SHARK_DB_PASS
* SHARK_DB_ADDR
* SHARK_DB_NAME


## Basic Heroku Deployment

### Local Database (not needed if connecting to a remote DB)
Create a new postgres db:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

Initialize the local postgres DB on heroku:
```bash
heroku run python manage.py create_db
heroku run python manage.py db migrate
```

Get info on the postgres DB:
```bash
heroku pg:info
```

### Helpful toolbelt commands for troubleshooting
Tell heroku that you need to run 1 dyno:
```bash
heroku ps:scale web=1
```

See that the web app is running:
```bash
heroku ps
```

See environment variables:
```bash
heroku config
```

Tail the logs:
```bash
heroku logs --tail
```
