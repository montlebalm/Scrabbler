from config import Config
import itertools

class Words():
    def __init__(self):
        self.words = {}
    
    def load(self):
        """Run through a list of words and create a sorted string from each 
        word's letters. Assign the sorted string as a key for all words that 
        share the same letters."""
        self.words = {}
        
        for line in open(Config.dictionary_filepath, 'r'):
            line = line.strip()
            line_sorted = ''.join(sorted(line))
            
            if line_sorted not in self.words:
                self.words[line_sorted] = []
            
            # Store the real words as a list
            # We need line_sorted as the key for fast lookup later
            self.words[line_sorted].append(line)
    
    def get_words(self, string, constraints=[]):
        """Get all words that can be made from any combination of letters in
        the provided string"""
        
        # Get unique combinations of all the letters
        combos = self.get_combinations(sorted(string))
        
        # Find all the words whose letters are in a combo
        real_words = [x for x in combos if x in self.words]
        
        # Find all the real words that match the sorted string
        matches = dict((k, self.words[k]) for k in real_words)
        
        # Apply the constraints
        final_matches = matches
        if len(constraints) > 0:
            final_matches = self.apply_constraints(matches, constraints)
        
        return final_matches
    
    def apply_constraints(self, matches, constraints):
        """Return the matches that comply with the specified constraints"""
        complying_words = dict()
        
        for k, v in matches.iteritems():
            complies = [x for x in v if self.word_meets_constraints(x, constraints)]

            if len(complies) > 0:
                complying_words[k] = complies
                
        return complying_words
    
    def word_meets_constraints(self, word, constraints):
        for con in constraints:
            if len(word) <= con[1] or word[con[1]] != con[0]:
                return False
                    
        return True
    
    def get_combinations(self, letters, min_len=2):
        """Get all unique combinations of the provided list of letters"""
        combos = []
        
        # Only look at letters equal to or greater than the min_len
        for i in xrange(min_len, len(letters) + 1):
            # Get unique combinations of letters and join into a string
            combos += [''.join(x) for x in itertools.combinations(letters, i)]
    
        return combos