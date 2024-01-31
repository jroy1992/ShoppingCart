import logging


class Item(object):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_item_price = round(self.quantity*self.price, 2)

    def update_quantity(self, quantity: int, add: bool=False, remove: bool=False):
        if add:
            self.quantity += quantity
        if remove:
            self.quantity -= quantity


class ShoppingCart(object):
    def __init__(self):
        self.total_items = {}

    def get_item(self, name: str) -> Item:
        item = self.total_items.get(name, None)
        if not item:
            logging.info(f'{name} not in cart')
            return

        logging.info(f'{item.name} -> Quantity:{item.quantity}, Price per {item.name}: {item.price}')
        return item

    def get_item_count(self, name: str) -> list:
        return self.total_items[name].quantity if name in self.total_items else 0

    def get_total_price(self) -> str:
        total_price = 0.00
        for item_name, item in self.total_items.items():
            total_price += round(item.price*item.quantity, 2)
        return "{:.2f}".format(total_price)
    
    def insert_item(self, name: str, price_per_item: float, quantity: int=1):
        item = Item(name=name, quantity=quantity, price=price_per_item)
        if item.name in self.total_items:
            self.total_items[name].update_quantity(quantity=quantity, add=True)
        else:
            self.total_items[name] = item 
    
    def delete_item(self, name: str, quantity: int=1):
        if name in self.total_items:
            item = self.total_items[name]
            if item.quantity > quantity:
                item.update_quantity(quantity=quantity, remove=True)
            elif item.quantity == quantity:
                self.total_items.pop(name)
            else:
                logging.info(f'Only {item.quantity} quantities of {name} are in cart')
                raise Exception(f'Only {item.quantity} quantities of {name} are in cart')
        else:
            logging.info(f'Item {name} not added to cart. Delete aborted!')
