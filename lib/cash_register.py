class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount:
            self.total -= (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0.0

    def remove_item(self):
        if self.items:
            removed_item = self.items.pop()
            for item in self.items:
                if item['title'] == removed_item:
                    self.total -= item['price'] * item['quantity']
                    break

    def get_items(self):
        return self.items
