from config import Config
import itertools

class Words():
    def __init__(self):
        self.words = {}
    
    def load(self):
        """Run through a list of words and create a sorted string from each word's
        letters. Assign the sorted string as a key for all words that share the
        same letters."""
        self.words = {}
        
        for line in open(Config.dictionary_filepath, 'r'):
            line = line.strip()
            line_sorted = ''.join(sorted(line))
            
            if line_sorted not in self.words:
                self.words[line_sorted] = []
            
            # Store the real words as a list
            # We need line_sorted as the key for fast lookup later
            self.words[line_sorted].append(line)
    
    def get_words(self, string, min_len=2):
        """Get all words that can be made from any combination of letters in
        the provided string"""
        
        # Get unique combinations of all the letters
        combos = self.get_combinations(sorted(string))
        
        # Find all the words whose letters are in a combo
        real_words = [x for x in combos if x in self.words]
        
        # Find all the real words that match the sorted string
        matches = dict((k, self.words[k]) for k in real_words)
        
        return matches
        
    def get_combinations(self, letters, min_len=2):
        """Get all unique combinations of the provided list of letters"""
        combos = []
        
        # Only look at letters equal to or greater than the min_len
        for i in xrange(min_len, len(letters) + 1):
            # Get unique combinations of letters and join into a string
            combos += [''.join(x) for x in itertools.combinations(letters, i)]
    
        return combos