
"""
Payment request includes
customerId, carRideId, amount, status
"""
class PaymentException(Exception):
    def __init__(self,  message=None, info=None) -> None:
        super().__init__(message)
        self.message = message or 'Account credit failed'
        self.details = info or {}

def is_payment_request_valid(payment_request):
    return all(x in payment_request for x in ['customerId', 'carRideId'])


def lambda_handler(event, context):
    if not is_payment_request_valid(event):
        raise ValueError('Invalid payment request')
    if event['customerId'].endswith('fail_payment'):
        raise PaymentException('Forced payment transaction failure')
    event['status'] = 'Completed'
    return event