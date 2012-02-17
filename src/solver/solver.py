from config import Config

class Solver():
	
	def get_word_value(self, word, tiles):
		"""Get the total value of a word"""
		value = 0
		word_mods = []
		letters = list(word)
		
		for i in range(len(letters)):
			let_val = Config.letters[letters[i]].value
			mod = tiles[i].modifier
			
			# Only add the letter mods if the tile is unused
			if tiles[i].letter == None:
				if mod == "DL":
					let_val *= 2
				elif mod == "TL":
					let_val *= 3
				elif mod == "DW" or mod == "TW":
					word_mods.append(mod)
				
			value += let_val
			
		total_value = value
		
		# Compute the mods that affect the entire word
		for mod in word_mods:
			if mod == "DW":
				total_value += value * 2
			elif mod == "TW":
				total_value += value * 3
			
		return value