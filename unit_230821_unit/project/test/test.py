from unittest import TestCase, main

from unit_230821_unit.project.library import Library


class TestLibrary(TestCase):

	def setUp(self):
		self.library=Library('New')

	def test_name_empty_raise_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.library.name=''

		self.assertEqual("Name cannot be empty string!", str(ve.exception))

	def test_name_works_prperly(self):
		self.assertEqual('New', self.library.name)

	def test_add_book_for_new_author(self):
		self.library.add_book('Duma', 'Gun')
		self.assertEqual({'Duma':['Gun']}, self.library.books_by_authors)

	def test_add_book_for_old_author_new_book(self):
		self.library.add_book('Duma', 'Gun')
		self.library.add_book('Duma', 'Top')
		self.assertEqual({'Duma':['Gun', 'Top']}, self.library.books_by_authors)

	def test_add_book_for_old_author_same_book(self):
		self.library.add_book('Duma', 'Gun')
		self.library.add_book('Duma', 'Gun')
		self.assertEqual({'Duma':['Gun']}, self.library.books_by_authors)

	def test_add_reader_already_exist(self):
		self.library.readers={'Ivan':[]}
		result=self.library.add_reader('Ivan')
		self.assertEqual("Ivan is already registered in the New library.", result)

	def test_add_reader_new(self):
		self.library.add_reader('Ivan')
		self.assertEqual({"Ivan":[]}, self.library.readers)

	def test_rent_book_non_existing_reader(self):
		result=self.library.rent_book('Ivan', 'Duma', 'Gun')
		self.assertEqual("Ivan is not registered in the New Library.", result)

	def test_rent_book_non_existing_author(self):
		self.library.add_reader('Ivan')
		result = self.library.rent_book('Ivan', 'Duma', 'Gun')
		self.assertEqual("New Library does not have any Duma's books.", result)

	def test_rent_book_non_existing_book(self):
		self.library.add_reader('Ivan')
		self.library.add_book('Duma', 'Gun')
		result = self.library.rent_book('Ivan', 'Duma', 'Top')
		self.assertEqual("""New Library does not have Duma's "Top\".""", result)

	def test_rent_book_works_properly(self):
		self.library.add_reader('Ivan')
		self.library.add_book('Duma', 'Gun')
		result = self.library.rent_book('Ivan', 'Duma', 'Gun')
		self.assertEqual({'Ivan': [{'Duma': 'Gun'}]}, self.library.readers)
		self.assertEqual({'Duma': []}, self.library.books_by_authors)



if __name__=="__main__":
	main()

