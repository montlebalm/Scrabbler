class Tile():
	modifier = None
	letter = None
	coord = None
	
	def __init__(self, coord):
		self.coord = coord
		
	def __str__(self):
		if self.letter:
			return "[" + self.letter + "]"
		else:
			if self.modifier is not None:
				return self.modifier
			else:
				return "[ ]"