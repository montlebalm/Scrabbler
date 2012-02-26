from word_finder import Word_finder
from play import Play
import dictionary

class Crawler():

	def __init__(self):
		self.finder = Word_finder()
		self.grid = []

	def get_plays(self, grid, letters, matches):
		plays = []
		self.grid = grid
		max_x_val = len(grid)
		max_y_val = len(grid[0])
		x_picker = lambda cx, cy, i: self.grid[cx + i][cy]
		y_picker = lambda cx, cy, i: self.grid[cx][cy + i]
		sorted_word = matches.sort(lambda x, y: cmp(len(x), len(y)))
		longest_word_length = len(sorted_word[-1])

		for x in xrange(max_x_val):
			for y in xrange(max_y_val):
				tile = grid[x][y]
				
				# Must start at a blank space
				if tile.letter is None:
					new_plays = []

					x_anchors = self.__get_anchors(tile.coord, max_x_val, x, len(letters), x_picker)
					y_anchors = self.__get_anchors(tile.coord, max_y_val, y, len(letters), y_picker)

					x_plays = self.__get_axis_plays(tile.coord, "x", x_anchors, letters)
					y_plays = self.__get_axis_plays(tile.coord, "y", y_anchors, letters)
					
					if y_plays and not x_anchors:
						pass
						
#						cross_x_plays = {}
#						
#						# Get all the cross plays
#						new_x = x + 1
#						while new_x <= x + longest_word_length:
#							new_coord = (new_x, tile.coord[1])
#							
#							new_y_anchors = self.__get_anchors(new_coord, max_y_val, tile.coord[0], len(letters), lambda cx, cy, i: self.grid[cx][cy + i])
#							new_y_plays = self.__get_axis_plays(new_coord, "y", new_y_anchors, letters)
#							
#							if new_y_plays:
#								# Look at each play
#								for play in new_y_plays:
#									# Look at each word
#									for word in play.words:
#										# We con only be adding 1 extra letter crossways
#										if len(word) == len(play.constraints) + 1:
#											if new_coord not in cross_x_plays:
#												cross_x_plays[new_coord] = []
#											
#											cross_x_plays[new_coord].append(play)
											
						# Find words using combinations of cross plays
						
					
					if x_anchors and not y_anchors:
						pass

					new_plays = x_plays + y_plays

					if new_plays:
						plays += new_plays

		return plays

	def __get_anchors(self, coord, max_axis_val, axis_val, reach, tile_picker):
		front_anchors = self.__get_front_anchors(coord, max_axis_val, axis_val, reach, tile_picker)
		rear_anchors = self.__get_rear_anchors(coord, max_axis_val, axis_val, tile_picker)

		return rear_anchors + front_anchors

	def __get_front_anchors(self, coord, max_axis, axis_val, reach, tile_picker):
		anchors = []
		length = reach
		ctr = 0

		while ctr <= length:
			if axis_val + ctr < max_axis:
				tile = tile_picker(coord[0], coord[1], ctr)
	
				if tile.letter:
					anchor = (tile.letter, ctr)
					anchors.append(anchor)
					length += 1
	
				ctr += 1
			else:
				break

		return anchors

	def __get_rear_anchors(self, coord, max_axis, axis_val, tile_picker):
		anchors = []
		letters = []
		axis_value = axis_val - 1
		ctr = 0

		# Get the anchors
		while axis_value >= 0:
			tile = tile_picker(coord[0], coord[1], ctr)

			if tile.letter:
				letters.append(tile.letter)
			else:
				break

			axis_value -= 1
			ctr += 1

		# Reverse the anchors and set indexes
		if letters:
			print letters
			anchors = [(l, i) for l, i in reversed(letters)]

		return anchors
	
	def __get_axis_plays(self, coord, axis, constraints, letters):
		plays = []

		num_con = len(constraints)
		# Get sets of constraints in ascending order
		# First set has 1 constraint, second has 2, etc
		constraint_lists = [constraints[0:num_con - i] for i in xrange(num_con)]

		for constraint_list in constraint_lists:
			# Get all constraint letters and add them to the base
			constraint_letters = [x[0] for x in constraint_list]
			match_letters = letters + ''.join(constraint_letters)

			# Find the words that work with our letters and constraints
			matches = self.finder.get_words(match_letters, constraint_list)

			# Assign each coordinate a list of words that can be played
			for match_words in matches.itervalues():
				# The word has to have more letters than we have constraints
				words = [x for x in match_words if len(x) > num_con]

				if words:
					p = Play(coord, words, axis)
					p.constraints = constraint_list
					plays.append(p)

		return plays