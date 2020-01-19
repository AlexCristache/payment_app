"""
Init the app
"""
# pylint: disable=C0103
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
if os.environ['DATABASE_URL']:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

from app import views # pylint: disable=c0413
