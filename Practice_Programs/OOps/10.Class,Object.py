#10. Order Status Tracker
'''Problem: Track order status updates.
Answer:'''

class Order:
    def __init__(self, order_id, status="Pending"):
        self.order_id = order_id
        self.status = status
    def update_status(self, new_status):
        self.status = new_status
    def show_status(self):
        print(f"Order {self.order_id} status: {self.status}")


# Create and update
o = Order("ORD123")
o.update_status("Shipped")