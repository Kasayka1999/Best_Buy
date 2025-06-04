import products as products_class


class Store:

    def __init__(self, product_list):
        self.products = product_list


    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for p in self.products:
            if product == p:
                self.products.pop()

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for p in self.products:
            quantity = products_class.Product.get_quantity(p)
            total_quantity += quantity
        return total_quantity


    def get_all_products(self):
        return self.products


    def order(self, shopping_list):
        total_price = 0
        for shop in shopping_list:
            price = products_class.Product.buy(shop[0],shop[1])
            total_price += price
        return f"Order cost {total_price} dollars"



def main():
    product_list = [products_class.Product("Iphone 16 Pro", price=1450, quantity=100),
                    products_class.Product("Earbuds", price=250, quantity=500),
                    products_class.Product("Macbook", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()