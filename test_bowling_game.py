import unittest
from bowling_game import *

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_gutterGame(self):
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)
    
    def test_allOnes(self):
        for i in range(20):
            self.game.roll(1)
        self.assertEqual(self.game.score(), 20)