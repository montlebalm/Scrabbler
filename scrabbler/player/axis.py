class Axis(object):
	name = ''
	tile_picker = None
	max_value = 0

	def __init__(self, name, tile_picker):
		self.name = name
		self.tile_picker = tile_picker