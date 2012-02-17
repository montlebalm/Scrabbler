import unittest
from words import words

class Test(unittest.TestCase):

#    def test_load(self):
#        d = words.Words()
#        d.load()
#        print "Loaded " + str(len(d.words)) + " dictionary words"
        
    def test_match(self):
        w = words.Words()
        w.load()
        matches = w.get_words('dictionary')
        print matches