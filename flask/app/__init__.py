"""
Init the app
"""
from flask import Flask

app = Flask(__name__) # pylint: disable=C0103

from app import views # pylint: disable=c0413
