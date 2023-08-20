from abc import ABC

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
	def __init__(self, table_number, capacity):
		self.table_number=table_number
		self.capacity=capacity
		self.food_orders=[]
		self.drink_orders=[]
		self.number_of_people=0
		self.is_reserved=False

	@property
	def capacity(self):
		return self.__capacity

	@capacity.setter
	def capacity(self, value):
		if value<=0:
			raise ValueError("Capacity has to be greater than 0!")
		self.__capacity=value

	def reserve(self, number_of_people):
		self.number_of_people+=number_of_people
		self.is_reserved=True

	def order_food(self, baked_food:BakedFood):
		self.food_orders.append(baked_food)

	def order_drink(self, drink:Drink):
		self.drink_orders.append(drink)

	def get_bill(self):
		bill=0
		if self.drink_orders:
			for d in self.drink_orders:
				bill+=d.price
		if self.food_orders:
			for f in self.food_orders:
				bill+=f.price

		return bill

	def clear(self):
		self.food_orders.clear()
		self.drink_orders.clear()
		self.is_reserved=False

	def free_table_info(self):
		if not self.is_reserved:
			result=[f"Table: {self.table_number}", f"Type: {__class__.__name__}", f"Capacity: {self.capacity}"]
			return "\n".join(result)


