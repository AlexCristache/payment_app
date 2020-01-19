"""
Init the app
"""
# pylint: disable=C0103, E0401, E0611
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#if os.environ['DATABASE_URL']:
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except KeyError:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payment_app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views # pylint: disable=c0413
