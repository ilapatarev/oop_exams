from project.table.table import Table


class InsideTable(Table):
	def __init__(self, table_number, capacity):
		super().__init__(table_number, capacity)

	@property
	def table_number(self):
		return self.__table_number

	@table_number.setter
	def table_number(self, value):
		if not 0<value<=50:
			raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
		self.__table_number=value

	def free_table_info(self):
		if not self.is_reserved:
			result=[f"Table: {self.table_number}", f"Type: {__class__.__name__}", f"Capacity: {self.capacity}"]
			return "\n".join(result)



