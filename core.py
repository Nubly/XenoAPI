from flask import Flask
from os import environ


# TODO: Productionize this, for now it's just better than committing secrets
SQL_USER = os.environ.get('XENOAPI_SQL_USER')
SQL_PASS = os.environ.get('XENOAPI_SQL_PASS')
SQL_HOST = os.environ.get('XENOAPI_SQL_HOST')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mariadb+mariadbconnector://{SQL_USER}:{SQL_PASS}@{SQL_HOST}:3306/hydro"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
