class Play():
	anchors = []
	cross_plays = []

	def __init__(self, coord, word, axis):
		self.coord = coord
		self.word = word
		self.axis = axis

	def __str__(self):
		output = 'Play "{0}"'.format(self.word)

		if self.cross_plays:
			crosses = ', '.join([x.word for x in self.cross_plays])
			output += ' (' + crosses + ')'

		output += ' at {0} on {1} axis'.format(
			self.coord,
			self.axis)

		if self.anchors:
			output += " with "

			for con in self.anchors:
				output += str(con)

		return output