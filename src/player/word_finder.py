import itertools
import dictionary

class Word_finder():
    
    def get_words(self, string, constraints=[]):
        """Get all hashed that can be made from any combination of letters in
        the provided string"""
        
        # Get unique combinations of all the letters
        combos = self.__get_combinations(sorted(string))
        
        # Find all the hashed whose letters are in a combo
        real_words = [x for x in combos if dictionary.is_key(x)]
        
        # Find all the real hashed that match the sorted string
        matches = dict((k, dictionary.get_words(k)) for k in real_words)
        
        # Apply the constraints
        if constraints:
            matches = self.__apply_constraints(matches, constraints)
        
        return matches
    
    def __apply_constraints(self, matches, constraints):
        """Return the matches that comply with the specified constraints"""
        complying_words = dict()
        
        for k, v in matches.iteritems():
            complies = [x for x in v if self.__meets_constraints(x, constraints)]

            if complies:
                complying_words[k] = complies
                
        return complying_words
    
    def __meets_constraints(self, word, constraints):
        for con in constraints:
            if len(word) <= con[1] or word[con[1]] != con[0]:
                return False
                    
        return True
    
    def __get_combinations(self, letters, min_len=2):
        """Get all unique combinations of the provided list of letters"""
        combos = []
        
        # Only look at letters equal to or greater than the min_len
        for i in xrange(min_len, len(letters) + 1):
            # Get unique combinations of letters and join into a string
            combos += [''.join(x) for x in itertools.combinations(letters, i)]
    
        return combos