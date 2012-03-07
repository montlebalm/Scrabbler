class Anchor(object):
	def __init__(self, letter, index):
		self.letter = letter
		self.index = index

	def __str__(self):
		return '({0}, {1})'.format(self.letter, self.index)

	def satisfied_by(self, word):
		return len(word) > self.index and word[self.index] == self.letter