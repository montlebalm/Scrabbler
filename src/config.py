from board import modifiers
from solver import letter

class Config:
	
	# Anagram
	dictionary_filepath = "../../dictionary.txt"
	
	# Board
	height = 15
	width = 15
	mods_nw = {
		(0, 3): modifiers.Modifier.TW,
		(0, 6): modifiers.Modifier.TL,
		(1, 2): modifiers.Modifier.DL,
		(1, 5): modifiers.Modifier.DW,
		(2, 1): modifiers.Modifier.DL,
		(2, 4): modifiers.Modifier.DL,
		(3, 0): modifiers.Modifier.TW,
		(3, 3): modifiers.Modifier.TL,
		(3, 7): modifiers.Modifier.DW,
		(4, 2): modifiers.Modifier.DL,
		(4, 6): modifiers.Modifier.DL,
		(5, 1): modifiers.Modifier.DW,
		(5, 5): modifiers.Modifier.TL,
		(6, 0): modifiers.Modifier.TL,
		(6, 4): modifiers.Modifier.DL
	}
	
	# Common
	letters = {
		'a': letter.Letter('a', 9, 1),
		'b': letter.Letter('b', 2, 3),
		'c': letter.Letter('c', 2, 3),
		'd': letter.Letter('d', 4, 2),
		'e': letter.Letter('e', 12, 1),
		'f': letter.Letter('f', 2, 4),
		'g': letter.Letter('g', 3, 2),
		'h': letter.Letter('h', 2, 4),
		'i': letter.Letter('i', 9, 1),
		'j': letter.Letter('j', 1, 8),
		'k': letter.Letter('k', 1, 5),
		'l': letter.Letter('l', 4, 1),
		'm': letter.Letter('m', 2, 3),
		'n': letter.Letter('n', 6, 1),
		'o': letter.Letter('o', 8, 1),
		'p': letter.Letter('p', 2, 3),
		'q': letter.Letter('q', 1, 10),
		'r': letter.Letter('r', 6, 1),
		's': letter.Letter('s', 4, 1),
		't': letter.Letter('t', 6, 1),
		'u': letter.Letter('u', 4, 1),
		'v': letter.Letter('v', 2, 4),
		'w': letter.Letter('w', 2, 4),
		'x': letter.Letter('x', 1, 8),
		'y': letter.Letter('y', 2, 4),
		'z': letter.Letter('z', 1, 10),
		' ': letter.Letter(' ', 2, 0)
	}