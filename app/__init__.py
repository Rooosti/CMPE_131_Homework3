from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app_obj.config.from_mapping(
        SECRET_KEY = 'mamas_secret_recipe_key',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
)

db = SQLAlchemy(app_obj)

from app import routes, models
