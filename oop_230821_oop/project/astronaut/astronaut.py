from abc import ABC, abstractmethod


class Astronaut(ABC):
	OXYGEN_CUNSUMPTION_PER_BREATHE=10
	def __init__(self, name, oxygen):
		self.name=name
		self.oxygen=oxygen
		self.backpack=[]

	@property
	def name(self):
		return  self.__name

	@name.setter
	def name(self, value):
		if value.strip()=='':
			raise ValueError("Astronaut name cannot be empty string or whitespace!")
		self.__name=value

	@abstractmethod
	def breathe(self):
		self.oxygen-=self.OXYGEN_CUNSUMPTION_PER_BREATHE

	def increase_oxygen(self, amount):
		self.oxygen+=amount
