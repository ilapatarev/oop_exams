from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):

	def setUp(self):
		self.shopping_cart=ShoppingCart("Stopcheto", 100)

	def test_correct_initializing(self):
		self.assertEqual("Stopcheto", self.shopping_cart.shop_name)
		self.assertEqual(100, self.shopping_cart.budget)
		self.assertEqual({}, self.shopping_cart.products)

	def test_props_not_correct_not_upper_first_letter_raise_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.shopping_cart.shop_name="stop"
		self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

	def test_props_not_contain_only_letters_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.shopping_cart.shop_name="S5top"
		self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

	def test_add_to_card_expensive_product_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.shopping_cart.add_to_cart('tv', 2000)

		self.assertEqual("Product tv cost too much!", str(ve.exception))

	def test_add_to_cart_work_properly(self):
		result=self.shopping_cart.add_to_cart('meat', 8)
		self.assertEqual({"meat":8}, self.shopping_cart.products)
		self.assertEqual("meat product was successfully added to the cart!", result)

	def test_remove_product_in_empty_cart_raise_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.shopping_cart.remove_from_cart('meat')

		self.assertEqual("No product with name meat in the cart!", str(ve.exception))

	def test_remove_correct_product(self):
		self.shopping_cart.products={"meat":8, "tv":1}
		result=self.shopping_cart.remove_from_cart("meat")
		self.assertEqual({"tv":1}, self.shopping_cart.products)
		self.assertEqual("Product meat was successfully removed from the cart!", result)

	def test_add_expect_new_cart(self):
		other=ShoppingCart('OOOO', 2000)
		self.shopping_cart.add_to_cart("from first", 1)
		other.add_to_cart('from second', 2)
		new=self.shopping_cart.__add__(other)
		self.assertEqual('StopchetoOOOO', new.shop_name)
		self.assertEqual(2100, new.budget)
		self.assertEqual({'from first':1, 'from second':2}, new.products)

	def test_buy_with_error(self):
		with self.assertRaises(ValueError) as ve:
			self.shopping_cart.products={"tv":100, "yt":200}
			self.shopping_cart.buy_products()

		self.assertEqual("Not enough money to buy the products! Over budget with 200.00lv!", str(ve.exception))

	def test_buy_products_correct_works(self):
		self.shopping_cart.products={"tv":20}
		result=self.shopping_cart.buy_products()
		self.assertEqual('Products were successfully bought! Total cost: 20.00lv.', result)

if __name__=="__main__":
	main()