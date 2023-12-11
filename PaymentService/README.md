# Payment Service

Simulate a payment occur or not depending of the customerID

The price is set at the end of the car ride, and Payment is the entity, with the supporting states: Open, UnderProcessing, Completed, Cancelled.

The payment keeps information of the customer ID, the transaction date and the car ride ID.

This is a mockup to support creating business exception like a payment could not complete.

## Implementation Choice

This is a lambda function with handler supporting submit payment operation. The component listen to queue. 
