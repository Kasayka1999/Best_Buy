import pytest
from products import Product

#for test purposes.
macbook = Product("MacBook Air M2", price=10, quantity=100)

# Empty name
def test_empty_name():
    with pytest.raises(TypeError):
        Product("", price=1450, quantity=100)

# Negative Price
def test_negative_price():
    with pytest.raises(TypeError):
        Product("MacBook Air M2", price=-10, quantity=100)

#Creating normal product
def test_normal_create():
    macbook_normal = Product("MacBook Air M2", price=10, quantity=100)

#test if 0 zero stock became inactive
def test_stock_zero():
    macbook.set_quantity(0)
    assert macbook.is_active() is False


#test if buy more than existing quantity raise typeerror
def test_buy_more_than_existing_quantity():
    with pytest.raises(TypeError):
        macbook.buy(1000)

#test if quantity changes after buy
def test_quantity_changes_after_buy():
    macbook2 = Product("MacBook Air M2", price=10, quantity=100)
    assert macbook2.buy(10) == 100.0 #return output after buy if correct
    assert macbook2.get_quantity() == 90 #remained quantity if correct