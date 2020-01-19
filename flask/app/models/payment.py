"""
The model for the SQLAlchemy payment object.
"""
# pylint: disable=R0903
#from app import db
from sqlalchemy import Column, Integer, String, DateTime

class Payment():
    """
    Payment class that abstracts the database schema which records the
    payments that were made.
    """
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    card_holder = Column(String(80), nullable=False)
    card_number = Column(String(16), nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    security_code = Column(String(3), nullable=True)
    amount = Column(Integer, nullable=False)
    attempted_date = Column(DateTime, nullable=False)


    def __init__(self, **kwargs):
        """
        Init the values for the newly create payment object.
        """
        valid_keys = ("amount", "card_holder", "card_number",
                      "expiration_date", "attempted_date", "security_code")
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
