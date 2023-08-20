class Player:
	names = []

	def __init__(self, name:str, age:int, stamina:int=100):
		self.name=name
		self.age=age
		self.stamina=stamina
		self.need_sustenance=True if self.stamina<100 else False

	def check_name_exist(self, name):

		if name in self.names:
			return True
		else:
			self.names.append(name)
			return False

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if value=='':
			raise ValueError("Name not valid!")
		elif self.check_name_exist(value):
			raise ValueError(f"Name {value} is already used!")
		self.__name=value

	@property
	def age(self):
		return  self.__age

	@age.setter
	def age(self, value):
		if value<12:
			raise ValueError("The player cannot be under 12 years old!")

		self.__age=value

	@property
	def stamina(self):
		return  self.__stamina

	@stamina.setter
	def stamina(self, value):
		if value<0 or value>100:
			raise ValueError("Stamina not valid!")
		self.__stamina=value

	def __str__(self):
		return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

