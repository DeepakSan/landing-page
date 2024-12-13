# landing-page

[![Python - 3.10](https://img.shields.io/pypi/pyversions/landing-page.svg?label=python%203.10)](https://www.python.org/downloads/release/python-310/)
[![Flask - Latest](https://img.shields.io/pypi/v/Flask.svg?label=flask%20latest)](https://pypi.org/project/Flask/)
[![Hatch - Latest](https://img.shields.io/pypi/v/hatch.svg?label=hatch%20latest)](https://pypi.org/project/hatch/)
[![SQLAlchemy - Latest](https://img.shields.io/pypi/v/SQLAlchemy.svg?label=sqlalchemy%20latest)](https://pypi.org/project/SQLAlchemy/)
[![Postgres - 14](https://img.shields.io/badge/Postgres-14-blue)](https://www.postgresql.org/docs/release/14/)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

Clone this repo
```console
touch .env
touch .flaskenv
```
Copy the contents of .env and .flaskenv in config templates 

```console
cp config_templates/.env .env
cp config_templates/.flaskenv .flaskenv```

Create a db in pgadmin4 and make changes to the DB_URI in .env and the username/password in docker-compose file

Now the site can be seen at 127.0.0.1:5000/
```console
docker-compose up -d
```
To stop

```console
docker-compose down
```


## License

`landing-page` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
