import unittest
from scrabbler import dictionary
from scrabbler.dictionary import loader

class Test(unittest.TestCase):

	def test_load(self):
		loader.load()

	# def test_match(self):
	# 	loader.load()
	# 	w = word_finder.Word_finder()

	# 	matches = w.get_words('tooth', [("h", 4)])
	# 	print matches

if __name__ == '__main__':
	unittest.main()