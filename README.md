# XenoAPI

GraphQL API code for the [Xenoponics](https://github.com/Nubly/Xenoponics) project.

Runs on a combination of Ariadne, FastAPI, and Flask.

## Requirements
- `python3 >= 3.11`

Databases used with this should be time-series, or should follow the following schema (for now):
| Key        | Variable type [default]         |
| :--        | :--                             |
| location	 | varchar(100)	                   |
| water_temp | float NULL	                   |
| air_temp	 | float                           |
| tds        | int(11)                         |
| humidity   | float                           |
| ph	     | float NULL                      |
| timestamp	 | timestamp [current_timestamp()] |


## Installation

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run it!

```shell
uvicorn handlers:app --interface wsgi --host 0.0.0.0
```
By default, this hosts on port 8000 via `uvicorn`.

Interface is configurable as well, I've just found the most success using [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) so far.

## GraphQL Methods/Endpoints

- `/api/v1/hydro`
  - GET: Currently returns a string telling you the API is working.
  - POST: Following the database schema, will insert the data into the DB
    - Returns JSON result of `graphql_sync` as well as status code

## TODO

- Streamline DB deployment
  - Provide files for replicatable schema setup
  - Containerize? Currently, just running stock mariadb container from Docker Hub
    - Could be templated to specify the DB connection type within `core.py`
- Document supported GraphQL queries/mutations further
- Add more GraphQL methods as necessary
- Publish OpenAPI spec
- Republish GraphQL playground

## Authors
Alex Denofre (@Nubly)
