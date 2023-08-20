from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
	def setUp(self):
		self.movie=Movie('Matrix', 1999, 9.6)
		self.movie.actors=['Reeves', 'An Mos']
		self.other=Movie('Star Wars', 2002, 9.5)

	def test_name_setter_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.movie.name=''

		self.assertEqual("Name cannot be an empty string!", str(ve.exception))

	def test_year_setter_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.movie.year=1886

		self.assertEqual("Year is not valid!", str(ve.exception))

	def test_add_actor_already_added_expect_comment(self):
		result=self.movie.add_actor('Reeves')
		self.assertEqual("Reeves is already added in the list of actors!", result)

	def test_add_actor_new_work_properly(self):
		self.movie.add_actor('Tom')
		self.assertEqual(['Reeves', 'An Mos', 'Tom'], self.movie.actors)

	def test_gt_our_movie_better(self):
		result=self.movie.__gt__(self.other)
		self.assertEqual('"Matrix" is better than "Star Wars"', result)

	def test_gt_other_movie_better(self):
		self.other.rating=9.9
		result=self.movie.__gt__(self.other)
		self.assertEqual('"Star Wars" is better than "Matrix"', result)

	def test_repr_method(self):
		result=self.movie.__repr__()
		self.assertEqual(
			'Name: Matrix\n'
			"Year of Release: 1999\n"
			"Rating: 9.60\n"
			"Cast: Reeves, An Mos",
			result
		)




if __name__=="__main__":
	main()


