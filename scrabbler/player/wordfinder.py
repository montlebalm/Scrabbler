import itertools
import scrabbler.dictionary

class WordFinder():

	def get_matches(self, string, constraints=[]):
		"""Get all hashed that can be made from any combination of letters in
		the provided string"""

		real_keys = self.__get_real_keys(string)
		matches = []

		if real_keys:
			# Find all the real hashed that match the sorted string
			matches = dict((k, scrabbler.dictionary.get_words(k)) for k in real_keys)

			# Apply the constraints
			if constraints:
				matches = self.__apply_constraints(matches, constraints)

		return matches

	def is_word(self, string):
		return scrabbler.dictionary.is_word(string)

	def get_words(self, string):
		output = []

		for words in self.__get_word_groups(string):
			output += [w for w in words]

		return output

	def __get_real_keys(self, string):
		# Get unique combinations of all the letters
		combos = self.__get_combinations(sorted(string))

		# Find all the hashed whose letters are in a combo
		real_keys = [x for x in combos if scrabbler.dictionary.is_key(x)]

		return real_keys

	def __apply_constraints(self, matches, constraints):
		"""Return the matches that comply with the specified constraints"""
		complying_words = dict()

		for k, v in matches.iteritems():
			complies = [x for x in v if self.__meets_constraints(x, constraints)]

			if complies:
				complying_words[k] = complies

		return complying_words

	def __meets_constraints(self, word, constraints):
		for con in constraints:
			if not con.satisfied_by(word):
				return False

		return True

	def __get_combinations(self, letters, min_len=2):
		"""Get all unique combinations of the provided list of letters"""
		combos = []

		# Only look at letters equal to or greater than the min_len
		for i in xrange(min_len, len(letters) + 1):
			# Get unique combinations of letters and join into a string
			combos += [''.join(x) for x in itertools.combinations(letters, i)]

		return combos