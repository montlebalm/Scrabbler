class Coord(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return '({0}, {1})'.format(self.x, self.y)