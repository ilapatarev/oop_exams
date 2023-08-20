from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):

	def setUp(self):
		self.bookstore=Bookstore(100)
		self.books={
			'a':2,
			'b':3,
		}

	def test_correct_initializing(self):
		self.assertEqual(100, self.bookstore.books_limit)
		self.assertEqual(0, self.bookstore.total_sold_books)
		self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

	def test_check_setter_expect_raise_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.bookstore.books_limit=0

		self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

	def test_len_of_the_books_in_store(self):
		self.bookstore.availability_in_store_by_book_titles=self.books
		result=self.bookstore.__len__()
		self.assertEqual(5, result)

	def test_receive_book_exceed_limit_raise_exception(self):
		self.bookstore.availability_in_store_by_book_titles=self.books
		with self.assertRaises(Exception) as ex:
			self.bookstore.receive_book('a', 150)

		self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))


	def test_receive_books_works_properly(self):
		self.bookstore.receive_book("b", 10)
		self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles['b'])

	def test_add_existing_book_correct(self):
		self.bookstore.availability_in_store_by_book_titles = {'a': 20}
		self.bookstore.receive_book('a', 50)
		self.assertEqual(70, self.bookstore.availability_in_store_by_book_titles['a'])

	def test_result_receive_books(self):
		result=self.bookstore.receive_book('a', 50)
		self.assertEqual("50 copies of a are available in the bookstore.", result)

	def test_sell_book_with_non_existing_book_raise_exception(self):
		with self.assertRaises(Exception) as ex:
			self.bookstore.sell_book('a', 2)

		self.assertEqual("Book a doesn't exist!", str(ex.exception))

	def test_sell_book_not_enough_copies_raise_exeption(self):
		self.bookstore.availability_in_store_by_book_titles={'a':100}
		with self.assertRaises(Exception) as ex:
			self.bookstore.sell_book('a', 200)

		self.assertEqual("a has not enough copies to sell. Left: 100", str(ex.exception))

	def test_sell_book_works_properly(self):
		self.bookstore.availability_in_store_by_book_titles={"a":100}
		result=self.bookstore.sell_book('a', 20)
		self.assertEqual(80, self.bookstore.availability_in_store_by_book_titles['a'])
		self.assertEqual(20, self.bookstore.total_sold_books)
		self.assertEqual("Sold 20 copies of a", result)

	def test_str_method(self):

		self.bookstore.availability_in_store_by_book_titles={'a':10, 'b':20}
		self.assertEqual(
			"Total sold books: 0\n"
			'Current availability: 30\n'
			" - a: 10 copies\n"
			" - b: 20 copies",
			self.bookstore.__str__()
		)



if __name__=="__main__":
	main()
