class Game(object):
    def __init__(self, score = 0):
        self._score = score

    def roll(self, pins):
        self._score += pins

    def score(self):
        return self._score