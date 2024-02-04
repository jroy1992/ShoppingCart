# ShoppingCart
Shopping cart package that helps keep track of number of items and prices.

## Insert item
Inserts item in the cart
```python
shoppingcart = ShoppingCart()
shoppingcart.insert_item(name='Apple', price_per_unit=1.50, quantity=10)
```

## Get item
```python
shoppingcart = ShoppingCart()
shoppingcart.insert_item(name='Apple', price_per_unit=1.50, quantity=10)
item = shoppingcart.get_item('Apple')
```

## Get item count
```python
shoppingcart = ShoppingCart()
shoppingcart.insert_item(name='Apple', price_per_unit=1.50, quantity=10)
count = shoppingcart.get_item_count('Apple')
```

## Get total price
```python
shoppingcart = ShoppingCart()
shoppingcart.insert_item(name='Apple', price_per_unit=1.50, quantity=10)
shoppingcart.insert_item(name='Mango', price_per_unit=2.50, quantity=10)
total_price = shoppingcart.get_total_price()
```

## Delete item
```python
shoppingcart = ShoppingCart()
shoppingcart.insert_item(name='Apple', price_per_unit=1.50, quantity=10)
shoppingcart.delete_item('Apple')
```
