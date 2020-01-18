"""
Define the app endpoints.
"""
import os
from app import app # pylint: disable=R0401

@app.route("/")
def index():
    """
    The home of the app.
    """
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container"

    return "Hello from Flask"
