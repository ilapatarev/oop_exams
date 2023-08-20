from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
	OXYGEN_CUNSUMPTION_PER_BREATHE = 15
	def __init__(self, name, oxygen=90):
		super().__init__(name, oxygen)

	def breathe(self):
		self.oxygen-=self.OXYGEN_CUNSUMPTION_PER_BREATHE