from Term_05.Best_Buy.products import LimitedProduct
from products import Product

class Store:

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for p in self.products:
            if product == p:
                self.products.pop()

    def get_total_quantity(self):
        total_quantity = 0
        for p in self.products:
            total_quantity += Product.get_quantity(p)
        return total_quantity

    def get_all_products(self):
        return self.products


    def order(self, shopping_list):
        cart_total_price = 0
        for shop in shopping_list:
            product_total_price = shop[0].buy(shop[1])  # Corrected
            cart_total_price += product_total_price
        return cart_total_price

