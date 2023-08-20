from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
	FOOD_TYPES = ['Bread', 'Cake']
	TABLE_TYPES = ['InsideTable', 'OutsideTable']
	DRINK_TYPES = ['Tea', 'Water']
	def __init__(self, name):
		self.name=name
		self.food_menu=[]
		self.drinks_menu=[]
		self.tables_repository=[]
		self.total_income=0



	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if value.strip()=='':
			raise ValueError("Name cannot be empty string or white space!")
		self.__name=value

	def add_food(self, food_type, name, price):
		if food_type in self.FOOD_TYPES:
			for f in self.food_menu:
				if f.name==name:
					raise Exception(f"{food_type} {name} is already in the menu!")
			if food_type=='Bread':
				self.food_menu.append(Bread(name, price))
			if food_type=='Cake':
				self.food_menu.append(Cake(name, price))
			return f"Added {name} ({food_type}) to the food menu"


	def add_drink(self, drink_type, name, portion, brand):
		if drink_type in self.DRINK_TYPES:
			for d in self.drinks_menu:
				if d.name==name:
					raise Exception(f"{drink_type} {name} is already in the menu!")
			if drink_type=='Tea':
				self.drinks_menu.append(Tea(name, portion, brand))
			elif drink_type=='Water':
				self.drinks_menu.append(Water(name, portion, brand))
			return f"Added {name} ({brand}) to the drink menu"

	def add_table(self, table_type, table_number, capacity):
		if table_type in self.TABLE_TYPES:
			for t in self.tables_repository:
				if t.table_number==table_number:
					raise Exception(f"Table {table_number} is already in the bakery!")
			if table_type=='InsideTable':
				self.tables_repository.append(InsideTable(table_number, capacity))
			elif table_type=='OutsideTable':
				self.tables_repository.append(OutsideTable(table_number, capacity))
			return f"Added table number {table_number} in the bakery"

	def reserve_table(self, number_of_people):
		not_find_table=True
		for t in self.tables_repository:
			if not t.is_reserved:
				if t.capacity>=number_of_people:
					t.reserve(number_of_people)
					not_find_table=False
					return f"Table {t.table_number} has been reserved for {number_of_people} people"

		if not_find_table:
			return f"No available table for {number_of_people} people"

	def order_food(self, table_number, *food_name:str):
		try:
			table=next(filter(lambda t: t.table_number==table_number, self.tables_repository))
		except StopIteration:
			raise Exception(f"Could not find table {table_number}")
		not_found_food = []
		for food in food_name:
			for f in self.food_menu:
				if f.name==food:
					table.order_food(f)
					break

			else:
				not_found_food.append(food)

		result=[f'Table {table_number} ordered:']
		for f in table.food_orders:
			result.append(repr(f))
		result.append(f'{self.name} does not have in the menu:')
		for f in not_found_food:
			result.append(f)
		return '\n'.join(result)

	def order_drink(self, table_number, *drink_name:str):
		try:
			table=next(filter(lambda t: t.table_number==table_number, self.tables_repository))
		except StopIteration:
			raise Exception(f"Could not find table {table_number}")
		not_found_drink = []
		for drink in drink_name:
			for d in self.drinks_menu:
				if d.name==drink:
					table.order_drink(d)
					break

			else:
				not_found_drink.append(drink)

		result=[f'Table {table_number} ordered:']
		for d in table.drink_orders:
			result.append(repr(d))
		result.append(f'{self.name} does not have in the menu:')
		for d in not_found_drink:
			result.append(d)
		return '\n'.join(result)

	def leave_table(self, table_number):
		table_bill=0
		for table in self.tables_repository:
			if table.table_number==table_number:

				table_bill=table.get_bill()
				self.total_income+=table_bill
				table.clear()

		return f"Table: {table_number}"'\n'f"Bill: {table_bill:.2f}"

	def get_free_tables_info(self):
		result=[]
		for t in self.tables_repository:
			if t.free_table_info():
				result.append(t.free_table_info())

		return '\n'.join(result)

	def get_total_income(self):
		return f'Total income: {self.total_income:.2f}lv'







