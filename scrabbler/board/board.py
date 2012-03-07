from tile import Tile
import config
import math

class Board():
	grid = []
	start = (0, 0)
	mods = {}

	def __init__(self):
		# Get the starting position
		start_x = int(math.floor(config.width / 2))
		start_y = int(math.floor(config.height / 2))
		self.start = (start_x, start_y)

		# Get each quadrant and combine
		mods_nw = config.mods_nw
		mods_ne = self.__rotate_mods(mods_nw, (0, 7))
		mods_se = self.__rotate_mods(mods_ne, (0, 7))
		mods_sw = self.__rotate_mods(mods_nw, (7, 0))
		self.mods = self.__combine_dicts(mods_nw, mods_sw, mods_ne, mods_se)

		# Construct the actual grid of tiles
		self.grid = self.__build(self.mods)

	def __str__(self):
		rows = ""

		for y in range(config.width):
			row = ""

			if y == 0:
				for x in range(config.height):
					space = "  " if x < 10 else " "
					row += "{0}{1}".format(x, space)

				row += "\n"

			for x in range(config.height):
				row += str(self.grid[x][y])

			rows += row + " " + str(y) + "\n"

		return rows

	def __combine_dicts(self, *args):
		combined = {}

		for arg in args:
			for k, v in arg.iteritems():
				combined[k] = v

		return combined

	def __rotate_mods(self, base, offset):
		quad = {}

		# Always use the NW quadrant as a base
		for coords, mod in base.iteritems():
			r = int(math.fabs(coords[0] - offset[0]) + offset[0])
			c = int(math.fabs(coords[1] - offset[1]) + offset[1])

			# Flip the order of the coords
			quad[(c, r)] = mod

		return quad

	def __build(self, mods):
		grid = []

		for x in range(config.height):
			grid.append([])

			for y in range(config.width):
				t = Tile(x, y)

				# See if these coords have a modifier
				if (x, y) in mods:
					t.modifier = mods[(x, y)]

				grid[x].append(t)

		return grid