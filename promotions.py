from abc import ABC, abstractmethod

class Promotion(ABC):
    """
    Promotion class using abstractmethod to not able to set Promotion if not Promotion type selected.
    """
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        return False


class SecondHalfPrice(Promotion):
    """
    Every second product for half price
    """
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        half_price_products = quantity // 2
        full_price_products = quantity - half_price_products
        return float(product.price * full_price_products) + (product.price * 0.5 * half_price_products)


class ThirdOneFree(Promotion):
    """
    Every third product is not calculating in total price.
    """
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        free_quantity = quantity // 3
        quantity -= free_quantity
        return float(product.price * quantity)

class PercentDiscount(Promotion):
    """
    Classic percentage discount.
    """
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return float(product.price * quantity * (1 - self.percent / 100))
