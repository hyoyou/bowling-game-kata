import unittest
from bowling_game import *

class TestBowlingGame(unittest.TestCase):
    def test_gutterGame(self):
        game = Game()
        for i in range(20):
            game.roll(0)
        self.assertEqual(game.score(), 0)
    
    def test_allOnes(self):
        game = Game()
        for i in range(20):
            game.roll(1)
        self.assertEqual(game.score(), 20)