from os import environ
import tomllib
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(f"{__name__}-default.yml")
# Override default settings with manual settings if exists
app.config.from_pyfile(f"{__name__}.yml", silent=True)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
