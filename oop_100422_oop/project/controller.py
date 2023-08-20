from project.player import Player
from project.supply.supply import Supply


class Controller:
	VALID_SUSTENANCE_TIPE=['Food', 'Drink']

	def __init__(self):
		self.players=[]
		self.supplies=[]

	def add_player(self, *args:Player):
		added_players=[]
		for player in args:
			if not player in self.players:
				self.players.append(player)
				added_players.append(player.name)

		return f"Successfully added: {', '.join(added_players)}"

	def add_supply(self, *args:Supply):
		for supply in args:
			self.supplies.append(supply)

	def sustain(self, player_name, sustenance_type:str):
		if sustenance_type not in self.VALID_SUSTENANCE_TIPE:
			return

		try:
			player=next(filter(lambda p: p.name==player_name, self.players))
		except:
			return

		no_supplies=True
		for supply in self.supplies:
			if supply.__class__.__name__==sustenance_type:
				no_supplies=False
		if no_supplies:
			raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

		for p in self.players:
			if p.name==player_name:
				if p.need_sustenance==False:
					return f"{player_name} have enough stamina."

		supply_name=''
		for p in self.players:
			if p.name==player_name:
				for s in reversed(self.supplies):
					if s.__class__.__name__==sustenance_type:
						supply_name=s.name
						if p.stamina+s.energy>100:
							p.stamina=100
							p.need_sustenance=False
						else:
							p.stamina+=s.energy
						self.supplies.remove(s)
						break
		return f"{player_name} sustained successfully with {supply_name}."

	def duel(self, first_player_name, second_player_name):
		first_player_no_stamina=False
		second_player_no_stamina=False
		first_player_stamina=0
		second_player_stamina=0

		for p in self.players:
			if p.name==first_player_name:
				first_player_stamina=p.stamina
				if p.stamina<=0:
					first_player_no_stamina=True
		for p in self.players:
			if p.name==second_player_name:
				second_player_stamina=p.stamina
				if p.stamina<=0:
					second_player_no_stamina=True

		if first_player_no_stamina and second_player_no_stamina:
			return f'{first_player_name} does not have enough stamina.\n{second_player_name} does not have enough stamina.'
		elif first_player_no_stamina:
			return f'{first_player_name} does not have enough stamina.'
		elif second_player_no_stamina:
			return f'{second_player_name} does not have enough stamina.'
		winner=''
		fp_after_duel_stamina=0
		sp_after_duel_stamina=0

		if first_player_stamina>second_player_stamina:
			for f in self.players:
				if f.name==first_player_name:
					for s in self.players:
						if s.name==second_player_name:


							f.need_sustenance = True
							if f.stamina -(s.stamina/2)<=0:
								f.stamina=0
								fp_after_duel_stamina = f.stamina
								winner=second_player_name
							else:
								f.stamina -= s.stamina / 2
								fp_after_duel_stamina = f.stamina
							break

			for s in self.players:
				if s.name==second_player_name:
					for f in self.players:
						if f.name==first_player_name:

							s.need_sustenance=True

							if s.stamina-(f.stamina/2)<=0:
								s.stamina=0
								sp_after_duel_stamina = s.stamina
								winner=first_player_name
							else:
								s.stamina -= f.stamina / 2
								sp_after_duel_stamina = s.stamina
							break

		if not winner:
			if fp_after_duel_stamina>sp_after_duel_stamina:
				winner=first_player_name
			else:
				winner=second_player_name
		if winner:
			return f"Winner: {winner}"

	def next_day(self):
		for p in self.players:

			if p.stamina-p.age*2<0:
				p.stamina=0
			else:
				p.stamina -= p.age * 2

		for p in self.players:
			for s in self.supplies:
				if s.__class__.__name__ == 'Food':

					if p.stamina+ s.energy > 100:
						p.stamina = 100
					else:
						p.stamina += s.energy
					self.supplies.remove(s)
					break

		for p in self.players:
			for s in self.supplies:
				if s.__class__.__name__ == 'Drink':
					p.stamina += s.energy
					if p.stamina + s.energy > 100:
						p.stamina = 100
					else:
						p.stamina += s.energy
					self.supplies.remove(s)
					break


	def __str__(self):
		info = []
		for p in self.players:
			info.append(p.__str__())
		for s in self.supplies:
			info.append(s.details())
		result = "\n".join(info)
		return result







