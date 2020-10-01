class AlivePlayer(Player):
	def __init__(self, name, color):
		Player.__init__(color)
		self.name = name 

	def make_move(self, available_moves, move):
		if move in available_moves > 0:
			return move
