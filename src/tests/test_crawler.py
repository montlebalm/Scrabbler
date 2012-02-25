import unittest
from board import board
from player import crawler
from dictionary import loader

class Test(unittest.TestCase):
	
	def test_crawl(self):
		loader.load()
		b = board.Board()
		
		# Add some test letters
		b.grid[0][8].letter = "t"   # hotel
		b.grid[1][8].letter = "o"
	#		b.grid[2][8].letter = "t"
	#		b.grid[3][8].letter = "e"
	#		b.grid[4][8].letter = "l"
	#		b.grid[0][11].letter = "p"  # play
	#		b.grid[1][11].letter = "l"
	#		b.grid[2][11].letter = "a"
	#		b.grid[3][11].letter = "y"
			
		print str(b)
		
		letters = "oh"
		c = crawler.Crawler()
		matches = c.get_words(letters)
		plays = c.get_plays(b.grid, letters, matches)
			
		for play in plays:
			print play
			print play.constraints
			
		print "We found {0} plays".format(len(plays))
			
		