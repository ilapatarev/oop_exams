from project.client import Client



class FoodOrdersApp:
	receipt_id=0

	def __init__(self, menu:list, clients_list:list):
		self.menu=[]
		self.clients_list=[]

	def register_client(self, client_phone_number:Client):
		if client_phone_number in self.clients_list:
			raise Exception("The client has already been registered!")
		self.clients_list.append(client_phone_number)
		return f"Client {client_phone_number} registered successfully."

	def add_meals_to_menu(self, *meals:Meal):
		for meal in meals:
			if meal ==Starter or meal==MainDish or meal == Dessert:
				self.menu.append(meal)

	def show_menu(self):
		if len(self.menu)<5:
			raise Exception("The menu is not ready!")
		for meal in self.menu:
			return meal.details()

	def add_meals_to_shopping_cart(self, client_phone_number:Client, **meal_names_and_quantities:Meal):
		if len(self.menu)<5:
			raise Exception("The menu is not ready!")

		if client_phone_number not in self.clients_list:
			self.clients_list.append(Client(client_phone_number))
		for meal in meal_names_and_quantities.keys():
			if meal not in self.menu:
				raise Exception(f"{meal} is not on the menu!")

		for meal_name, meal_quantity in meal_names_and_quantities.items():
			for meal in self.menu:
				if meal.name==meal_name:
					if meal.quantity>=meal_quantity:
						client_phone_number.shopping_cart.append(meal)
						client_phone_number.bill+=meal.price*meal_quantity

		for meal_name, meal_quantity in meal_names_and_quantities.items():
			for meal in self.menu:
				if meal.name==meal_name:
					meal.quantity-=meal_quantity

		return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client_phone_number.shopping_cart)} " \
               f"for {client_phone_number.bill:.2f}lv."


	def cancel_order(self, client_phone_number):
		if not client_phone_number.shopping_cart:
			raise Exception("There are no ordered meals!")

		client_phone_number.shopping_cart=[]
		client_phone_number.bill=0

		return f"Client {client_phone_number} successfully canceled his order."

	def finish_order(self, client_phone_number):
		if not client_phone_number.shopping_cart:
			raise Exception("There are no ordered meals!")

		total_paid_money=client_phone_number.bill
		client_phone_number.shopping_cart=[]
		client_phone_number.bill=0
		self.receipt_id+=1
		return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."


	def __str__(self):
		return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
