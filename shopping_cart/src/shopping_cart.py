#!/usr/bin/env python

import logging


class Item(object):
    """
    Object to handle item properties in the shopping cart.
    Handles the logic to update quantity if same item is re-added to/removed from the cart

    Args:
        name (str): Name of the item to be added to cart
        price (float): Price per unit of the item to be added to cart
        quantity (int): Quantity of the item to be added to cart

    Attributes:
        name (str): Name of the item to be added to cart
        price (float): Price per unit of the item to be added to cart
        quantity (int): Quantity of the item to be added to cart
        total_item_price (float): Total price of all units of the item
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_item_price = round(self.quantity*self.price, 2)

    def update_quantity(self, quantity: int, add: bool=False, remove: bool=False) -> None:
        """
        Updates the quantity of the item base on addition or removal
        :param quantity: Quantity by which to be updated
        :param add: Add the quantity to existing quantity
        :param remove: Remove the quantity from existing quantity
        :return: None
        """
        if add:
            self.quantity += quantity
        if remove:
            self.quantity -= quantity


class ShoppingCart(object):
    """
    Object to handle shopping cart operations.
    Set of logics to handle getting/ inserting/ deleting items, querying item count and total price of items in cart.

    Attributes:
        total_items (dict): Dict of names of items in the cart mapped against the Item object
    """
    def __init__(self):
        self.total_items = {}

    def get_item(self, name: str) -> Item:
        """
        Returns the item object if the item is in cart. Returns None if item not present.
        :param name: Name of the item to get from cart
        :return: Item object of the item
        """
        return self.total_items.get(name, None)

    def get_item_count(self, name: str) -> int:
        """
        Returns count of the item present in cart based on item name. If item not present, returns 0
        :param name: Name of the item to get count for
        :return: Count of the item, 0 if not present
        """
        return self.total_items[name].quantity if name in self.total_items else 0

    def get_total_price(self) -> str:
        """
        Returns total price of the items in cart in two decimal float format
        :return: total price of items
        """
        total_price = 0.00
        for item_name, item in self.total_items.items():
            total_price += item.total_item_price
        return "{:.2f}".format(total_price)
    
    def insert_item(self, name: str, price_per_unit: float, quantity: int=1) -> None:
        """
        Inserts item into the shopping cart
        :param name: Name of the item to insert
        :param price_per_unit: Price of per unit of the item
        :param quantity: Quantity of item to add to cart
        :return: None
        """
        if name in self.total_items:
            self.total_items[name].update_quantity(quantity=quantity, add=True)
        else:
            self.total_items[name] = Item(name=name, quantity=quantity, price=price_per_unit)
    
    def delete_item(self, name: str, quantity: int=1) -> None:
        """
        Deletes item from cart. Raises exception if item not present in cart or if quantity to delete is greater
        than quantity available.
        :param name: Name of the item to delete
        :param quantity: Quantity of item to delete
        :return: None
        """
        if name in self.total_items:
            item = self.total_items[name]
            if item.quantity > quantity:
                item.update_quantity(quantity=quantity, remove=True)
            elif item.quantity == quantity:
                self.total_items.pop(name)
            else:
                raise ValueError(f'Only {item.quantity} quantities of {name} are in cart. Attempted deleting {quantity}')
        else:
            raise KeyError(f'Item {name} not added to cart. Delete aborted!')
