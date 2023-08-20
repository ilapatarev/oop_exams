from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
	OXYGEN_CUNSUMPTION_PER_BREATHE = 5
	def __init__(self, name, oxygen=70):
		super().__init__(name, oxygen)

	def breathe(self):
		self.oxygen-=self.OXYGEN_CUNSUMPTION_PER_BREATHE


