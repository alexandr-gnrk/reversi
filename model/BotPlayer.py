from random import randint

class AlivePlayer(Player):
	def __init__(self, color):
		Player.__init__(color) 

	def make_move(self, available_moves):
		if len(available_moves > 0):
			return available_moves[randint(0, len(available_moves))]
