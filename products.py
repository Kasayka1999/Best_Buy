import promotions

class Product:

    def __init__(self, name, price, quantity):
        if not isinstance(price, (int, float)) or not isinstance(quantity, (int, NonStockedProduct)) or price < 0 or quantity < 0:
            raise TypeError("Price and Quantity must be a positive number. (ex: Price: 12.5 (float or int) // Quantity: 5 (only int)")
        if not name:
            raise TypeError("Name can't be empty")
        self.name = name
        self.price = price
        self.quantity = quantity
        self._promotion = None #if not setted a promotion always return none

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
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.get_promotion_name()}"

    def buy(self, quantity):
        """
        calculating the price based on stock, or promotion.
        """
        if isinstance(self, NonStockedProduct):
            if self._promotion:
                return self._promotion.apply_promotion(self, quantity)
            else:
                return float(self.price * quantity)

        if quantity > self.quantity or quantity < 0:
            raise TypeError(f"Quantity larger than what exists. Available Stock = {self.quantity}")
        else:
            self.quantity -= quantity
            if self._promotion:
                return self._promotion.apply_promotion(self, quantity)
            else:
                total_price = float(self.price * quantity)
                return total_price

    def set_promotion(self, promotion):
        """
        this works as a command to set the the promotion on specific product.
        """
        self._promotion = promotion

    def get_promotion_name(self):
        return self._promotion.name if self._promotion else "None"

class NonStockedProduct(Product):
    """
    Type for the products without Quantity limits like Digital Products
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited, Promotion: {self.get_promotion_name()}"

    def is_active(self):
        return True #return True because should be an active product when we ordering from menu


class LimitedProduct(Product):
    """
    Limited products, able to add maximum purchase limit per order.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        calculating the price based on stock, or promotion.
        """
        if quantity > self.quantity or quantity > self.maximum: # if exceed maximum limit or no stock, raise an error.
            raise TypeError(f"Only 1 is allowed from this product!")
        else:
            self.quantity -= quantity
            if self._promotion:
                return self._promotion.apply_promotion(self, quantity)
            else:
                total_price = float(self.price * quantity)
                return total_price

    def show(self):
        if Product.is_active(self):
            return f"{self.name}, Price: {self.price}, Limited to 1 per order!, Promotion: {self.get_promotion_name()}"