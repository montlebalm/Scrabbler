import unittest
from scrabbler.dictionary import loader
from scrabbler.board import board
from scrabbler.player import crawler

class Test(unittest.TestCase):

	def test_crawl(self):
		loader.load()
		b = board.Board()

		# Add some test letters
		b.grid[2][8].letter = "l"
		b.grid[1][7].letter = "n"

		print str(b)

		letters = "e"
		c = crawler.Crawler()
		plays = c.get_plays(b.grid, letters)

		for play in plays:
			print play

		print "We found {0} plays".format(len(plays))

if __name__ == '__main__':
	unittest.main()