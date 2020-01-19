"""
The model for the SQLAlchemy payment object.
"""
# pylint: disable=R0903,E0401
from app import db

class Payment(db.Model):
    """
    Payment class that abstracts the database schema which records the
    payments that were made.
    """
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    card_holder = db.Column(db.String(80), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    security_code = db.Column(db.String(3), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    attempted_date = db.Column(db.DateTime, nullable=False)


    def __init__(self, **kwargs):
        """
        Init the values for the newly create payment object.
        """
        valid_keys = ("amount", "card_holder", "card_number",
                      "expiration_date", "attempted_date", "security_code")
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))


    def save_record(self):
        """
        Save the current record in the db.
        """
        db.session.add(self)
        db.session.commit()
