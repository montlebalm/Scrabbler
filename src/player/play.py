class Play():
    constraints = []
    
    def __init__(self, coord, words, axis):
        self.coord = coord
        self.words = words
        self.axis = axis
        
    def __str__(self):
        return "Play at {0} on {1} axis using {2}".format(self.coord, self.axis, self.words)