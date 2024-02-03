import unittest
import shopping_cart


def _common_setup(instance: unittest.TestCase):
    instance.item_name = 'Apple'
    instance.item_price = 10.05
    instance.item_quantity = 15
    instance.add_quantity = 10
    instance.remove_quantity = 5
    instance.items_list = [
        ('Rice', 2.54, 1),
        ('Cereal', 5.23, 2),
        ('Banana', 7.00, 4)
    ]


class TestItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _common_setup(instance=cls)

    def test_item_creation(self):
        item = shopping_cart.Item(name=self.item_name, price=self.item_price, quantity=self.item_quantity)
        self.assertEqual(item.name, self.item_name)
        self.assertEqual(item.price, self.item_price)
        self.assertEqual(item.quantity, self.item_quantity)

    def test_update_quantity(self):
        item = shopping_cart.Item(name=self.item_name, price=self.item_price, quantity=self.item_quantity)
        item.update_quantity(quantity=self.add_quantity, add=True)
        self.assertEqual(item.quantity, self.item_quantity+self.add_quantity)

        item.quantity = self.item_quantity
        item.update_quantity(quantity=self.remove_quantity, remove=True)
        self.assertEqual(item.quantity, self.item_quantity-self.remove_quantity)


class TestShoppingCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _common_setup(instance=cls)

    def test_insert_item_default_quantity(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price)

        self.assertEqual(cart.total_items[self.item_name].name, self.item_name)
        self.assertEqual(cart.total_items[self.item_name].quantity, 1)
        self.assertEqual(cart.total_items[self.item_name].price, self.item_price)

    def test_insert_item_multiple_quantity(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price, quantity=self.item_quantity)

        self.assertEqual(cart.total_items[self.item_name].name, self.item_name)
        self.assertEqual(cart.total_items[self.item_name].quantity, self.item_quantity)
        self.assertEqual(cart.total_items[self.item_name].price, self.item_price)

    def test_insert_multiple_items(self):
        cart = shopping_cart.ShoppingCart()
        for (name, price, quantity) in self.items_list:
            cart.insert_item(name=name, price_per_unit=price, quantity=quantity)

        self.assertEqual(len(cart.total_items), len(self.items_list))
        for (name, price, quantity) in self.items_list:
            self.assertEqual(cart.total_items[name].name, name)
            self.assertEqual(cart.total_items[name].price, price)
            self.assertEqual(cart.total_items[name].quantity, quantity)

    def test_insert_multiple_same_item(self):
        cart = shopping_cart.ShoppingCart()
        additions = 3
        for i in range(additions):
            cart.insert_item(name=self.item_name, price_per_unit=self.item_price, quantity=self.item_quantity)

        self.assertEqual(len(cart.total_items), 1)
        self.assertEqual(cart.total_items[self.item_name].quantity, self.item_quantity*additions)

    def test_get_item(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price, quantity=self.item_quantity)

        item = cart.get_item(self.item_name)
        self.assertEqual(item.name, self.item_name)
        self.assertEqual(item.price, self.item_price)
        self.assertTrue(item.quantity, self.item_quantity)

    def test_item_count(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price, quantity=45)

        self.assertEqual(cart.get_item_count(self.item_name), 45)

    def test_delete_item_default_quantity(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price)

        cart.delete_item(self.item_name)
        self.assertEqual(len(cart.total_items), 0)

    def test_delete_item_multiple_quantity(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price, quantity=self.item_quantity)

        cart.delete_item(self.item_name, quantity=self.item_quantity)
        self.assertEqual(len(cart.total_items), 0)

    def test_delete_item_exceeded_quantity(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name=self.item_name, price_per_unit=self.item_price, quantity=self.item_quantity)

        with self.assertRaises(Exception):
            cart.delete_item(self.item_name, 100)

    def test_total_price(self):
        cart = shopping_cart.ShoppingCart()
        for (name, price, quantity) in self.items_list:
            cart.insert_item(name=name, price_per_unit=price, quantity=quantity)

    @unittest.expectedFailure
    def test_get_nonexistent_item(self):
        cart = shopping_cart.ShoppingCart()
        cart.get_item('Onion')

    @unittest.expectedFailure
    def test_delete_nonexistent_item(self):
        cart = shopping_cart.ShoppingCart()
        cart.delete_item('Onion')

    @unittest.expectedFailure
    def test_delete_exceeded_item_quantity(self):
        cart = shopping_cart.ShoppingCart()
        cart.insert_item(name='Onion', price_per_unit=1.35, quantity=10)
        cart.delete_item(name='Onion', quantity=20)


if __name__ == '__main__':
    unittest.main()
