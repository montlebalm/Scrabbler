from scrabbler.player import wordfinder, play, anchor, axis
import scrabbler.dictionary

class Crawler():
	finder = wordfinder.WordFinder()

	def __init__(self):
		# Setup the x and y axis values
		# We'll use these to prevent duplicating our X and Y queries
		self.axies = {
			'x': axis.Axis('x', lambda c, i: self.grid[c.x + i][c.y]),
			'y': axis.Axis('y', lambda c, i: self.grid[c.x][c.y + i])}

	def get_plays(self, grid, letters):
		plays = []
		self.grid = grid

		# Setup the axies
		self.axies['x'].max_value = len(grid)
		self.axies['y'].max_value = len(grid[0])

		# Store a list of all the words we can make
		self.matches = self.finder.get_matches(letters)

		for x in xrange(self.axies['x'].max_value):
			for y in xrange(self.axies['y'].max_value):
				tile = grid[x][y]

				# Must start at a blank space
				if tile.letter is None:
					new_plays = []

					# Get the regular plays along the x and y axis
					new_plays += self.__get_anchored_plays(tile.coord, "x", letters)
					new_plays += self.__get_anchored_plays(tile.coord, "y", letters)

					# Get the plays that don't attach to any letters on the given axis
					new_plays += self.__get_unanchored_plays(tile.coord, "x")
					new_plays += self.__get_unanchored_plays(tile.coord, "y")

					if new_plays:
						plays += new_plays

		# Uniqueify the plays
		unique_plays = self.__get_unique_plays(plays)

		return unique_plays

	def __get_cross_plays(self, starting_play, axis, player_letters):
		opp_axis = self.__get_opposite_axis(axis)
		letter_indexes = [x.index for x in player_letters]
		valid = True
		cross_words = [] # All the words that are made on the opp axis
		cross_plays = []

		for i in letter_indexes:
			opp_anchors = self.__get_anchors(starting_play.coord, opp_axis, 1)

			if opp_anchors:
				# Find the word we've made with our anchors
				anchor_word = self.__get_anchor_word(opp_anchors, starting_play.word[i])

				#if anchor_word: print "Checking on " + anchor_word + " (" + str(self.finder.is_word(anchor_word)) + ")"

				# Add the new cross play if we've made a dictionary word
				if anchor_word and self.finder.is_word(anchor_word):
					cross_words.append(anchor_word)
				else:
					valid = False
					break

		# If all the newly made words are valid, add them as plays
		if valid:
			for word in cross_words:
				cross_play = play.Play(starting_play.coord, word, opp_axis)
				cross_plays.append(cross_play)

		return {
			"valid": valid,
			"cross_plays": cross_plays}

	def __get_anchor_word(self, anchors, letter):
		word = ''
		ctr = 0
		hasUsedLetter = False

		# Find the word we've made with our anchors
		while ctr < len(anchors):
			# If the anchor's index doesn't match the current index
			# then this must be the new letter
			if ctr != anchors[ctr].index:
				anchors.insert(ctr, anchor.Anchor(letter, ctr))
				hasUsedLetter = True

			word += anchors[ctr].letter
			ctr += 1

		# If we reached the end and haven't used out letter, add it to the end
		if hasUsedLetter == False:
			word += letter
			hasUsedLetter = True

		return word

	def __get_anchors(self, coord, axis, reach):
		'''Get both the front and the rear anchors for the given axis and coordinate'''
		front_anchors = self.__get_front_anchors(coord, axis, reach)
		rear_anchors = self.__get_rear_anchors(coord, axis)

		return rear_anchors + front_anchors

	def __get_front_anchors(self, coord, axis, reach):
		'''Find the letters ahead of (right or below) the given coordinate on the given axis'''
		anchors = []
		length = reach
		axis_val = getattr(coord, axis)
		ctr = 0

		while ctr <= length:
			if axis_val + ctr < self.axies[axis].max_value:
				tile = self.axies[axis].tile_picker(coord, ctr)

				if tile.letter:
					anchors.append(anchor.Anchor(tile.letter, ctr))
					length += 1

				ctr += 1
			else:
				break

		return anchors

	def __get_rear_anchors(self, coord, axis):
		'''Find the letters behind (left or above) the given coordinate on the given axis'''
		anchors = []
		letters = []
		axis_val = getattr(coord, axis)
		ctr = -1

		while axis_val + ctr >= 0:
			tile = self.axies[axis].tile_picker(coord, ctr)

			if tile.letter:
				# Add the new letters to the front instead of the back
				# This is because we're going backwards
				letters.insert(0, tile.letter)
			else:
				break

			ctr -= 1

		for i in xrange(len(letters)):
			anchors.append(anchor.Anchor(letters[i], i))

		return anchors

	def __get_anchored_plays(self, coord, axis, letters):
		'''Find all the plays for the provided axis that originate at the given coordinate'''
		plays = []
		opp_axis = self.__get_opposite_axis(axis)
		anchors = self.__get_anchors(coord, axis, len(letters))
		num_con = len(anchors)

		# Get sets of constraints in ascending order
		# First set has 1 constraint, second has 2, etc
		anchor_lists = [anchors[0:num_con - i] for i in xrange(num_con)]

		for anchor_list in anchor_lists:
			# Get all constraint letters and add them to the base
			anchor_letters = [x.letter for x in anchor_list]
			match_letters = letters + ''.join(anchor_letters)

			# Find the words that work with our letters and constraints
			matches = self.finder.get_matches(match_letters, anchor_list)

			# Assign each coordinate a list of words that can be played
			for match_words in matches.itervalues():
				# The word has to have more letters than we have constraints
				words = [x for x in match_words if len(x) > num_con]

				for word in words:
					# Make sure the word doesn't hang over the edge of the grid
					if len(word) + getattr(coord, axis) < self.axies[axis].max_value:
						new_play = play.Play(coord, word, axis)
						new_play.anchors = anchor_list
						player_letters = self.__get_player_letters(word, new_play.anchors)

						result = self.__get_cross_plays(new_play, axis, player_letters)

						if result['valid']:
							new_play.cross_plays = result['cross_plays']
							plays.append(new_play)

		return plays

	def __get_player_letters(self, word, anchors):
		'''Get anchors of all the letters in the word that weren't already anchors'''
		letters = []
		anchor_indexes = [x.index for x in anchors]

		for i in xrange(len(word)):
			# If this letters is not one of the contraints
			# it must be the player's
			if i not in anchor_indexes:
				letters.append(anchor.Anchor(word[i], i))

		return letters

	def __get_unanchored_plays(self, coord, axis):
		'''Find all the plays that don't have an anchor on their primary axis'''
		plays = []

		# Look over every possible word we can make
		for match in self.matches:
			# Setup a dummy play that we'll use to find cross plays
			possible_play = play.Play(coord, match, axis)
			# Find all the plays along the opposite axis
			cross_plays = self.__get_cross_plays(possible_play, axis)

			if cross_plays:
				possible_play.cross_plays = cross_plays
				plays.append(possible_play)

		return plays

	def __get_unique_plays(self, plays):
		'''Sift out all the duplicate plays'''
		seen = dict()
		unique_plays = []

		for play in plays:
			if play.coord not in seen:
				seen[play.coord] = play.word
				unique_plays.append(play)

		return unique_plays

	def __get_opposite_axis(self, axis):
		return 'x' if axis == 'y' else 'y'