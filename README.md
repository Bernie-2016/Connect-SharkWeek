# Connect-SharkWeek
Public API for [Sharknado](https://github.com/Bernie-2016/Connect-Sharknado) using the
[JSON API 1.0 Spec](http://jsonapi.org/)
[Newsfeed spec](https://github.com/Bernie-2016/Connect-SharkWeek/issues/3)

## Development
Make sure you have the following installed:
* postgresql 9.4
* python 3.4

It's also recommended that you use
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

To set up the DB for local development:
```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_data
```

To start the app in local development mode:
```sh
$ python ./runserver.py
```

## Production
App configuration is currently defined in the `/opt/bernie/config.yml`
file, which shares the same config settings as
[Sharknado](https://github.com/Bernie-2016/Connect-Sharknado).

### Sample config
```yaml
postgresql:
    dbname: __postgres__
    dbuser: __user__
    dbpass: __pass__
    host: __host__
    port: 5432

flask:
    host: 127.0.0.1
```
