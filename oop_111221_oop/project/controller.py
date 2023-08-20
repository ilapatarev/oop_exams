from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
	VALID_CAR_TYPES=["MuscleCar", "SportsCar"]
	def __init__(self):
		self.cars=[]
		self.drivers=[]
		self.races=[]


	def create_car(self, car_type, model, speed_limit):
		for car in self.cars:
			if car.model==model:
				raise Exception(f"Car {model} is already created!")

		if car_type in self.VALID_CAR_TYPES:
			if car_type=="SportsCar":
				self.cars.append(SportsCar(model, speed_limit))
			else:
				self.cars.append(MuscleCar(model, speed_limit))
			return f"{car_type} {model} is created."

	def create_driver(self, driver_name):
		for d in self.drivers:
			if d.name==driver_name:
				raise Exception(f"Driver {driver_name} is already created!")

		self.drivers.append(Driver(driver_name))
		return f"Driver {driver_name} is created."

	def create_race(self, race_name):
		for r in self.races:
			if r.name==race_name:
				raise Exception(f"Race {race_name} is already created!")

		self.races.append(Race(race_name))
		return f"Race {race_name} is created."

	def add_car_to_driver(self, driver_name, car_type):
		try:
			driver = next(filter(lambda d: d.name == driver_name, self.drivers))
		except StopIteration:
			raise Exception(f"Driver {driver_name} could not be found!")
		car=None
		if car_type in self.VALID_CAR_TYPES:
			for c in reversed(self.cars):

				if c.__class__.__name__==car_type:
					if c.is_taken:
						continue
					else:
						car=c
						break


		else:
			raise Exception(f"Car {car_type} could not be found!")
		if not car:
			raise Exception(f"Car {car_type} could not be found!")

		if driver.car:
			old_model=driver.car.model
			driver.car.is_taken=False
			driver.car=car
			car.is_taken=True
			return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

		else:
			driver.car = car
			car.is_taken = True
			return f"Driver {driver_name} chose the car {car.model}."

	def add_driver_to_race(self, race_name, driver_name):
		try:
			race=next(filter(lambda r: r.name==race_name, self.races))
		except StopIteration:
			raise Exception(f"Race {race_name} could not be found!")

		try:
			driver = next(filter(lambda d: d.name == driver_name, self.drivers))
		except StopIteration:
			raise Exception(f"Driver {driver_name} could not be found!")

		if not driver.car:
			raise Exception(f"Driver {driver_name} could not participate in the race!")
		else:
			if driver in race.drivers:
				return f"Driver {driver_name} is already added in {race_name} race."
			else:
				race.drivers.append(driver)
				return f"Driver {driver_name} added in {race_name} race."

	def start_race(self, race_name):
		try:
			race=next(filter(lambda r: r.name==race_name, self.races))
		except StopIteration:
			raise Exception(f"Race {race_name} could not be found!")

		if len(race.drivers)<3:
			raise Exception(f"Race {race_name} cannot start with less than 3 participants!")


		first_name=''
		first_max_speed=0
		second_name=''
		second_max_speed=0
		third_name=''
		third_max_speed=0
		for d in race.drivers:
			if d.car.speed_limit>first_max_speed:
				first_max_speed=d.car.speed_limit
				first_name=d.name

		for d in race.drivers:
			if d.car.speed_limit>second_max_speed and d.car.speed_limit<first_max_speed :
				second_max_speed=d.car.speed_limit
				second_name=d.name

		for d in race.drivers:
			if d.car.speed_limit>third_max_speed and d.car.speed_limit<second_max_speed :
				third_max_speed=d.car.speed_limit
				third_name=d.name

		for d in self.drivers:
			if d.name==first_name or d.name==second_name or d.name==third_name:
				d.number_of_wins+=1

		return f"Driver {first_name} wins the {race_name} race with a speed of {first_max_speed}.\nDriver {second_name} wins the {race_name} race with a speed of {second_max_speed}.\nDriver {third_name} wins the {race_name} race with a speed of {third_max_speed}."













