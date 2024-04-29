'''
Implement the OrderStatus class, which describes a flag with the states of online orders. The flag must have three elements:

ORDER_PLACED
PAYMENT_RECEIVED
SHIPPING_COMPLETE
'''

from enum import Flag

class OrderStatus(Flag):
    ORDER_PLACED = 1
    PAYMENT_RECEIVED = 2
    SHIPPING_COMPLETE = 4

# Example
order_status = OrderStatus(0)
order_status |= OrderStatus.ORDER_PLACED

if OrderStatus.ORDER_PLACED in order_status:
    print('Order placed!')

order_status |= OrderStatus.PAYMENT_RECEIVED

if OrderStatus.PAYMENT_RECEIVED in order_status:
    print('Payment received!')

order_status |= OrderStatus.SHIPPING_COMPLETE

if OrderStatus.SHIPPING_COMPLETE in order_status:
    print('Shipping complete!')

# Output
# Order placed!
# Payment received!
# Shipping complete!