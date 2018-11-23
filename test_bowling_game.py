import unittest
from bowling_game import *

class TestBowlingGame(unittest.TestCase): 
    def test_gameClass(self):
        self.assertTrue(isinstance(Game(), Game))