from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
	def __init__(self):
		self.planet_repository=PlanetRepository()
		self.astronaut_repository=AstronautRepository()
		self.valid_astronaut_types=["Biologist", "Geodesist", "Meteorologist"]
		self.successful_missions=0
		self.non_compl_missions=0

	def add_astronaut(self, astronaut_type, name):
		if astronaut_type not in self.valid_astronaut_types:
			raise Exception("Astronaut type is not valid!")
		for a in self.astronaut_repository.astronauts:
			if a.name==name:
				return f"{name} is already added."

		if astronaut_type=="Biologist":
			self.astronaut_repository.astronauts.append(Biologist(name))
		elif astronaut_type=="Geodesist":
			self.astronaut_repository.astronauts.append(Geodesist(name))
		elif astronaut_type=="Meteorologist":
			self.astronaut_repository.astronauts.append(Meteorologist(name))
		return f"Successfully added {astronaut_type}: {name}."

	def add_planet(self, name, items):
		for p in self.planet_repository.planets:
			if p.name==name:
				return  f"{name} is already added."

		self.planet_repository.planets.append(Planet(name))
		items=list(items.split(', '))
		for p in self.planet_repository.planets:
			if p.name==name:
				for i in items:
					p.items.append(i)
		return f"Successfully added Planet: {name}."

	def retire_astronaut(self, name):
		try:
			astro=next(filter(lambda a: a.name==name, self.astronaut_repository.astronauts))
		except SpaceStation:
			raise Exception(f"Astronaut {name} doesn't exist!")

		self.astronaut_repository.astronauts.remove(astro)
		return  f"Astronaut {name} was retired!"

	def recharge_oxygen(self):
		for a in self.astronaut_repository.astronauts:
			a.oxygen+=10

	def send_on_mission(self, planet_name):
		try:
			planet=next(filter(lambda p: p.name==planet_name, self.planet_repository.planets))
		except StopIteration:
			raise Exception("Invalid planet name!")

		astro_for_mission=[]
		for a in self.astronaut_repository.astronauts:
			if a.oxygen>30:
				astro_for_mission.append(a)

		if not astro_for_mission:
			raise Exception("You need at least one astronaut to explore the planet!")

		new_astro_for_mission=sorted(astro_for_mission, key=lambda a: a.oxygen, reverse=True )
		if len(new_astro_for_mission)>5:
			new_astro_for_mission=new_astro_for_mission[:4]
		is_m_success=False
		for a in new_astro_for_mission:
			if a.oxygen>0:
				if len(planet.items)>0:
					for i in reversed(planet.items):
						a.backpack.append(i)
						planet.items.remove(i)
						a.breathe()
						if a.oxygen>0 and len(planet.items)>0:
							continue
						else:
							break
				else:
					is_m_success=True
					break
			else:
				continue
		if is_m_success:
			self.successful_missions+=1
			return f"Planet: {planet_name} was explored. {len(new_astro_for_mission)} astronauts participated in collecting items."
		else:
			self.non_compl_missions+=1
			return  "Mission is not completed."

	def report(self):
		result=[f'{self.successful_missions} successful missions!', f'{self.non_compl_missions} missions were not completed!', 'Astronauts info:']
		for a in self.astronaut_repository.astronauts:
			result.append(f'Name: {a.name}')
			result.append(f'Oxygen: {a.oxygen}')
			result.append(f'Backpack items: {", ".join(a.backpack) if len(a.backpack)>0 else "none"}')

		return '\n'.join(result)

		
