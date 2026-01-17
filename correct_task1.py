# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.



def calculate_average_order_value(orders):
    total = 0
    #count = len(orders)  this counts all orders including cancelled ones
    count=0

    for order in orders:
        if order.get("status") != "cancelled":
            amount=order.get("amount")
            if isinstance(amount,(int,float)):
                total += amount
                count += 1

    if count == 0:
        return 0

    return total / count