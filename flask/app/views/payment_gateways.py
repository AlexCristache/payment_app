"""
Simple mocks of the payment gateways.
"""
import random

choices = (True, False)

class CheapPaymentGateway:
    """
    Process payments fro amounts < 20.
    """
    @staticmethod
    def is_busy():
        """
        Return whether the gateway is busy.
        """
        return random.choice(choices)


    @staticmethod
    def process_payment(payment):
        """
        Process the payment.
        """
        return random.choice(choices)


class ExpensivePaymentGateway:
    """
    Process payments for 20 < amount < 500.
    """
    @staticmethod
    def is_busy():
        """
        Return whether the gateway is busy.
        """
        return random.choice(choices)


    @staticmethod
    def process_payment(payment):
        """
        Process the payment.
        """
        return random.choice(choices)


class PremiumPaymentGateway:
    """
    Process payments > 500.
    """
    @staticmethod
    def is_busy():
        """
        Whether it's busy.
        """
        return random.choice(choices)


    @staticmethod
    def process_payment(payment):
        """
        Process the payment.
        """
        processed = False
        retry = 3
        while retry > 0 and not processed:
            processed = random.choice(choices)
            retry -= 1
        return processed
