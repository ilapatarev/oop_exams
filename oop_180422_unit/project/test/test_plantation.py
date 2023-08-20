from project.plantation import Plantation
from unittest import TestCase, main

class TestPlantation(TestCase):
	def setUp(self):
		self.farm=Plantation(2)
		self.farm.workers=['Ivan', 'Dragan']
		self.farm.plants={'Ivan':['one'], 'Dragan':["two"]}

	def test_correct_initializing(self):
		self.assertEqual(2, self.farm.size)
		self.assertEqual({'Ivan':['one'], 'Dragan':["two"]}, self.farm.plants)
		self.assertEqual(['Ivan', 'Dragan'], self.farm.workers)

	def test_property_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.farm.size=-1

		self.assertEqual("Size must be positive number!", str(ve.exception))

	def test_hire_worker_already_hired_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.farm.hire_worker('Ivan')
		self.assertEqual("Worker already hired!", str(ve.exception))

	def test_hire_worker_properly_works(self):
		result=self.farm.hire_worker('Pesho')
		self.assertEqual("Pesho successfully hired.", result)
		self.assertEqual(['Ivan', 'Dragan', 'Pesho'], self.farm.workers)

	def test_if_len_works_properly(self):
		self.assertEqual(2, self.farm.__len__())

	def test_planting_non_existing_worker_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.farm.planting('Gosho', 'three')

		self.assertEqual("Worker with name Gosho is not hired!", str(ve.exception))

	def test_if_len_bigger_than_size_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.farm.planting('Ivan', 'three')

		self.assertEqual("The plantation is full!", str(ve.exception))

	def test_planting_works_properly_with_existing_worker(self):
		self.farm.size=5
		result=self.farm.planting('Ivan', 'three')
		self.assertEqual({'Ivan':['one', 'three'], 'Dragan':['two']}, self.farm.plants )
		self.assertEqual("Ivan planted three.", result)

	def test_planting_works_properly_with_new_worker(self):
		self.farm.size = 5
		self.farm.hire_worker('Gosho')
		result=self.farm.planting('Gosho', 'three')
		self.assertEqual({'Ivan': ['one'], 'Dragan': ['two'], 'Gosho':['three']}, self.farm.plants)
		self.assertEqual("Gosho planted it's first three.", result)

	def test_str_works_properly(self):
		self.farm.size=5
		self.farm.planting('Ivan', 'three')
		result=self.farm.__str__()
		self.assertEqual(
			"Plantation size: 5\n"
			"Ivan, Dragan\n"
			"Ivan planted: one, three\n"
			"Dragan planted: two", result
		)

	def test_repr_works_properly(self):
		result=self.farm.__repr__()
		self.assertEqual(
			"Size: 2\n"
			'Workers: Ivan, Dragan', result
		)


if __name__=="__main__":
	main()