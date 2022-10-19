# XenoAPI

GraphQL API code for the [Xenoponics](https://github.com/Nubly/Xenoponics) project.

Runs on a combination of Ariadne, MariaDB, and Flask.

## Requirements
- `python3 >= 3.8`
- MariaDB or other SQL DB you'd like to enter information into
  - TODO: Include that in this project? Containerize it, include `podman` files for `podman play kube` or something 
- Ability to install things from PyPI

The SQL database should follow the following schema (for now):
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

## Authors
Alex Denofre
