from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
	def setUp(self):
		self.team=Team('Ajax')
		self.team.members={'Ivan':40, 'Vladi':11}
		self.other=Team('Other')
		self.other.members={"Maria":39}

	def test_correct_initializing(self):
		self.assertEqual('Ajax', self.team.name)
		self.assertEqual({'Ivan':40, 'Vladi':11}, self.team.members)

	def test_setter_digit_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.team.name="15min"
		self.assertEqual("Team Name can contain only letters!", str(ve.exception))

	def test_setter_symbol_expect_value_error(self):
		with self.assertRaises(ValueError) as ve:
			self.team.name="**min"
		self.assertEqual("Team Name can contain only letters!", str(ve.exception))

	def test_add_new_member(self):
		result=self.team.add_member(Tom=12, Pat=20)
		self.assertEqual({'Ivan':40, 'Vladi':11, 'Tom':12, 'Pat':20}, self.team.members)
		self.assertEqual("Successfully added: Tom, Pat", result)

	def test_add_new_member_no_members(self):
		self.team.members={}
		result=self.team.add_member(Tom=12, Pat=20)
		self.assertEqual({'Tom':12, 'Pat':20}, self.team.members)
		self.assertEqual("Successfully added: Tom, Pat", result)

	def test_add_existing_member(self):
		result=self.team.add_member(Ivan=40)
		self.assertEqual({'Ivan': 40, 'Vladi': 11}, self.team.members)
		self.assertEqual("Successfully added: ", result)

	def test_remove_member_non_existing(self):
		result=self.team.remove_member('Maria')
		self.assertEqual("Member with name Maria does not exist", result)

	def test_remove_member_existing(self):
		result=self.team.remove_member('Ivan')
		self.assertEqual("Member Ivan removed", result)
		self.assertEqual({'Vladi':11}, self.team.members)

	def test_gt_if_we_are_greater(self):
		result=self.team.__gt__(self.other)
		self.assertEqual(True, result)

	def test_gt_if_we_are_less(self):
		self.other.add_member(Eli=8, Niki=16)
		result=self.team.__gt__(self.other)
		self.assertEqual(False, result)

	def test_len_works_properly(self):
		result=self.team.__len__()
		self.assertEqual(2, result)
		self.other.add_member(Eli=8, Niki=16)
		result2=self.other.__len__()
		self.assertEqual(3, result2)

	def test_add_works_properl(self):
		result=self.team.__add__(self.other)
		self.assertEqual('AjaxOther', result.name )
		self.assertEqual({'Ivan':40, 'Vladi':11, "Maria":39}, result.members)


	def test_str_works_properly(self):
		result=self.team.__str__()
		self.assertEqual(
			"Team name: Ajax\n"
			"Member: Ivan - 40-years old\n"
			"Member: Vladi - 11-years old",
			result

		)

if __name__=="__main__":
	main()