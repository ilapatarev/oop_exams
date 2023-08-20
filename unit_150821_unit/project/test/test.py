from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
	def setUp(self):
		self.petshop=PetShop('New')


	def test_correct_initialization(self):
		self.assertEqual('New', self.petshop.name)
		self.assertEqual({}, self.petshop.food)
		self.assertEqual([], self.petshop.pets)

	def test_add_food_quantity_zero_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.petshop.add_food('New', 0)
		self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

	def test_add_food_properly_works_new(self):
		result=self.petshop.add_food('New', 1)
		self.assertEqual({'New':1}, self.petshop.food)
		self.assertEqual("Successfully added 1.00 grams of New.", result)
		self.assertEqual(1.00, self.petshop.food['New'])

	def test_add_food_works_second(self):
		self.petshop.food={'New':1}
		result2=self.petshop.add_food('Baf', 2)
		self.assertEqual("Successfully added 2.00 grams of Baf.", result2)
		self.assertEqual({'New':1, 'Baf':2}, self.petshop.food)
		self.assertEqual(2.00, self.petshop.food['Baf'])

	def test_add_food_existing_food(self):
		self.petshop.food={'New':1, 'Baf':2}
		result1=self.petshop.add_food('New', 10)
		self.assertEqual({'New': 11, 'Baf': 2}, self.petshop.food)
		self.assertEqual("Successfully added 10.00 grams of New.", result1)
		self.assertEqual(11.00, self.petshop.food['New'])

	def test_add_pet_new(self):
		result=self.petshop.add_pet('Sharo')
		self.assertEqual(['Sharo'], self.petshop.pets)
		self.assertEqual("Successfully added Sharo.", result)
		result2=self.petshop.add_pet('Matsa')
		self.assertEqual(['Sharo', 'Matsa'], self.petshop.pets)
		self.assertEqual("Successfully added Matsa.", result2)

	def test_add_pet_with_same_name_expect_exception(self):
		with self.assertRaises(Exception) as ex:
			self.petshop.pets=['Sharo']
			self.petshop.add_pet('Sharo')
		self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

	def test_feed_pet_no_pet_name_expect_exception(self):
		with self.assertRaises(Exception) as ex:
			self.petshop.feed_pet('New', 'Sharo')

		self.assertEqual("Please insert a valid pet name", str(ex.exception))

	def test_feed_pet_no_food_name(self):
		self.petshop.pets=['Sharo']
		result=self.petshop.feed_pet('New', 'Sharo')
		self.assertEqual('You do not have New', result)

	def test_feed_pet_not_enough_food(self):
		self.petshop.add_pet('Sharo')
		self.petshop.add_food('New', 50)
		result=self.petshop.feed_pet('New', 'Sharo')
		self.assertEqual("Adding food...", result)
		self.assertEqual(1050, self.petshop.food['New'])

	def test_feed_pet_enough_food(self):
		self.petshop.add_pet('Sharo')
		self.petshop.add_food('New', 500)
		result = self.petshop.feed_pet('New', 'Sharo')
		self.assertEqual("Sharo was successfully fed", result)
		self.assertEqual(400, self.petshop.food['New'])

	def test_repr_method(self):
		self.petshop.pets = ['Sharo', 'Matsa']
		self.assertEqual(
			'Shop New:\n'
			'Pets: Sharo, Matsa', self.petshop.__repr__()
		)

	def test_repr_method_no_pets(self):
		self.petshop.pets = []
		self.assertEqual(
			'Shop New:\n'
			'Pets: ', self.petshop.__repr__()
		)





if __name__=='__main__':
	main()
