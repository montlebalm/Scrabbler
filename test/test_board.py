import unittest

class Test(unittest.TestCase):

	def test_build(self):
		from board import board
		
		b = board.Board()
		b.print_board()