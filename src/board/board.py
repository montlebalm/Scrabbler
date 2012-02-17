from tile import Tile
from config import Config
import math

class Board():
	grid = []
	width = Config.width
	height = Config.height
	start = (0, 0)
	mods = {}
	
	def __init__(self):
		# Get the starting position
		start_x = int(math.floor(self.width / 2))
		start_y = int(math.floor(self.height / 2))
		self.start = (start_x, start_y)
		
		# Get each quadrant and combine
		mods_nw = Config.mods_nw
		mods_ne = self.rotate_mods(mods_nw, (7, 0))
		mods_se = self.rotate_mods(mods_ne, (7, 0))
		mods_sw = self.rotate_mods(mods_nw, (0, 7))
		self.mods = self.combine_dicts(mods_nw, mods_sw, mods_ne, mods_se)
		
		# Construct the actual grid of tiles
		self.grid = self.build(self.mods)
	
	def combine_dicts(self, *args):
		combined = {}
		
		for arg in args:
			for k, v in arg.iteritems():
				combined[k] = v
		
		return combined
	
	def rotate_mods(self, base, offset):
		quad = {}
		
		# Always use the NW quadrant as a base
		for coords, mod in base.iteritems():
			r = int(math.fabs(coords[0] - offset[0]) + offset[0])
			c = int(math.fabs(coords[1] - offset[1]) + offset[1])
	
			# Flip the order of the coords
			quad[(c, r)] = mod
			
		return quad
	
	def print_board(self):
		for rn in range(self.height):
			row = ""
			
			for cn in range(self.width):
				row += str(self.grid[rn][cn])
				
			print row
	
	def build(self, mods):
		grid = []
		
		for rn in range(self.height):
			grid.append([])
			
			for cn in range(self.width):
				t = Tile(rn, cn)
				
				# See if these coords have a modifier
				if (rn, cn) in mods:
					t.modifier = mods[(rn, cn)]
					
				grid[rn].append(t)
		
		return grid
	
	def get_letter_count(self, letter):
		count = 0
		
		for tile in self.grid:
			if tile.letter == letter:
				count += 1
		
		return count