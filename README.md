# landing-page

[![Python](https://img.shields.io/pypi/pyversions/landing-page.svg?label=python%203.10)](https://www.python.org/downloads/release/python-3100/)
[![Flask](https://img.shields.io/pypi/v/Flask.svg?label=flask%20latest)](https://pypi.org/project/Flask/)
[![Hatch](https://img.shields.io/pypi/v/hatch.svg?label=hatch%20latest)](https://pypi.org/project/hatch/)
[![SQLAlchemy](https://img.shields.io/pypi/v/SQLAlchemy.svg?label=sqlalchemy%20latest)](https://pypi.org/project/SQLAlchemy/)
[![Postgres](https://img.shields.io/badge/Postgres-14-blue)](https://www.postgresql.org/docs/release/14/)
[![Docker](https://img.shields.io/badge/Docker-latest-blue)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-latest-blue)](https://docs.docker.com/compose/)
[![HTML](https://img.shields.io/badge/HTML5-latest-blue)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS3-latest-blue)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-latest-blue)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)


-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

Clone this repo
```console
git clone <>
```

Create environment files in your local

```console
touch .env
touch .flaskenv
```
Copy the contents of .env and .flaskenv in config templates 

```console
cp config_templates/.env .env
cp config_templates/.flaskenv .flaskenv
```
Create a db in pgadmin4 and make changes to the 
1) DB_URI in .env
2) username/password in docker-compose file
3) API_KEY in .env


The steps below is to run via docker
```console
docker-compose up -d
```

Now the site can be seen at 127.0.0.1:5000/

To stop

```console
docker-compose down
```

The steps below is to run in local via hatch

```console
hatch env create
hatch run dev:build
<or>
hatch run prod:build
```

## License

`landing-page` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
