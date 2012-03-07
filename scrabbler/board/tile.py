from scrabbler.board import coord

class Tile():
	modifier = None
	letter = None
	coord = None

	def __init__(self, x, y):
		self.coord = coord.Coord(x, y)

	def __str__(self):
		if self.letter:
			return "[" + self.letter + "]"
		else:
			if self.modifier is not None:
				return self.modifier
			else:
				return "[ ]"