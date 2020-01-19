"""
Define the app endpoints.
"""
import os
import sqlite3
from flask import request, Flask, g
from app import app # pylint: disable=R0401
from app.models.payment import Payment

__all__ = ["index", "process_payment"]
#app = Flask(__name__)

DATABASE = 'payment_app.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """
    The home of the app.
    """
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container"

    return "Hello from Flask"


@app.route("/payment/create", methods=['GET', 'POST'])
def process_payment():
    """
    Process payment creation.
    """
    if request.method == 'GET':
        return "Get request"

    data = request.get_json()
    if data:
        print(data)

    return data, 200
