import products
import store
from Term_05.Best_Buy.products import NonStockedProduct, LimitedProduct

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)


def show_menu():
    """
    user menu interface
    """
    print(f"\n   Store Menu   \n"
          f"   ----------   \n"
          f"1. List all products in store\n"
          f"2. Show total amount in store\n"
          f"3. Make an order\n"
          f"4. Quit")

def show_list_products():
    """
    show all the active products in store inventory
    """
    print("-" * 5)
    index_count = 1
    for product in product_list:
        if product.is_active(): #checking if product is active (stock)
            print(f"{index_count}. {product.show()}")
            index_count += 1
    print("-" * 5)


def main():
    while True:
        """ user choice menu loop """
        show_menu()
        choice = input("Please choose a number: ")
        if choice == "1":
            show_list_products()

        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")
        elif choice == "3":
            show_list_products()
            print("When you want to finish order, enter empty text.")
            order_list = []
            while True:
                get_product = input("Which product # do you want?: ")
                if not get_product:
                    break  # Empty input: finish loop

                get_amount = input("What amount do you want?: ")

                if get_product.isdigit() and get_amount.isdigit():
                    found = False
                    index_count = 1
                    for product in product_list:
                        if product.is_active():
                            if int(get_product) == index_count:
                                order_list.append((product, int(get_amount)))
                                index_count += 1
                                print("Product added to list!\n")
                                found = True
                                break  # No need to keep looping
                            index_count += 1
                    if not found:
                        print(f"Error adding product!\n")
                else:
                    print(f"Error adding product!\n")
            try:
                if order_list:
                    message = best_buy.order(order_list)
                    print(f"********\nOrder made! Total payment: ${message}")
            except TypeError as e:
                print(f"Error while making order! {e}")

        elif choice == "4":
            print("Good bye!")
            break
        else:
            print("Error with your choice! Try again!")



if __name__ == "__main__":
    main()