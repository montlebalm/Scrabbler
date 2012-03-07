import unittest
from scrabbler import dictionary
from scrabbler.dictionary import loader

class Test(unittest.TestCase):

	def test_load(self):
		print "Starting load..."
		loader.load()
		print "...Finished"

	# def test_match(self):
	# 	loader.load()
	# 	w = word_finder.WordFinder()

	# 	matches = w.get_words('tooth', [("h", 4)])
	# 	print matches

if __name__ == '__main__':
	unittest.main()