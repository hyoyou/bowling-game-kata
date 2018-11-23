import unittest
from bowling_game import *

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def roll_many(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

    def test_gutterGame(self):
        self.roll_many(0, 20)
        self.assertEqual(self.game.score(), 0)
    
    def test_allOnes(self):
        self.roll_many(1, 20)
        self.assertEqual(self.game.score(), 20)
