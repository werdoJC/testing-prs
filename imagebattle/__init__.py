from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('imagebattle.config')

db = SQLAlchemy(app) 
from . import hooks  # noqa
from .import views  # noqa
from .import model

