class Product:

    def __init__(self, name, price, quantity):
        if not isinstance(price, (int, float)) or not isinstance(quantity, int) or price < 0 or quantity < 0:
            raise TypeError("Price and Quantity must be a positive number. (ex: Price: 12.5 (float or int) // Quantity: 5 (only int)")
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        Product.is_active(self)

    def is_active(self):
        if self.quantity > 0:
            return True
        else:
            return False

    def activate(self):
        Product.set_quantity(self,1)

    def deactivate(self):
        Product.set_quantity(self, 0)

    def show(self):
        if Product.is_active(self):
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity > self.quantity or quantity < 0:
            raise TypeError(f"Quantity larger than what exists. Available Stock = {self.quantity}")
        else:
            self.quantity -= quantity
            total_price = float(self.price * quantity)
            return total_price
