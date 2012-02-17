class Tile():
	modifier = None
	letter = None
	row = None
	col = None
	
	def __init__(self, row, col):
		self.row = row
		self.col = col
		
	def __str__(self):
		if self.modifier is not None:
			return self.modifier
		else:
			return "[]"