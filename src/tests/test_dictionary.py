import unittest
from dictionary import loader
from player import word_finder

class Test(unittest.TestCase):

#    def test_load(self):
#        d = words.Dictionary()
#        d.load()
#        print "Loaded " + str(len(d.words)) + " dictionary words"
        
    def test_match(self):
        loader.load()
        w = word_finder.Word_finder()
        
        matches = w.get_words('tooth', [("h", 4)])
        print matches