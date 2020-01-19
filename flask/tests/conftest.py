"""
Create the pytest fixtures to be used across all tests.
"""
import os
import tempfile

import pytest

from flask import Flask

app = Flask(__name__)

@pytest.fixture
def client():
    """
    Fixture that simulates the app.
    """
    db_fd, app.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as c:
        with app.app_context():
            app.init_db()
        yield c
    os.close(db_fd)
    os.unlink(app.config['SQLALCHEMY_DATABASE_URI'])
