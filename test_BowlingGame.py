import unittest
from BowlingClass import BowlingGame # importing bowling game class

class BowlingGameTests(unittest.TestCase):
    def throw_many(self, game, number_of_times, pins):
        for _ in range(number_of_times):
            game.throw(pins)

# changed equals to equal
    def test_all_gutters(self):
        game = BowlingGame()
        self.throw_many(game, 20 ,0 )
        game.calculate_score()
        self.assertEqual(game.score,0)
        """
            Testing function for an all 0 score
        """

    def test_perfect_game(self):
        game = BowlingGame()
        self.throw_many(game, 12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)
        """
            Testing function for all frames to knock 10 frames
        """
    def test_all_ones(self): #fixed indent error
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        self.throw_many(game, number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)
        """
            Testing function for checking if game = 20 points are all frames = 1
        """

    def test_different_throws (self):
        game = BowlingGame()
        game.throw(6)
        game.throw(0)
        game.throw(7)
        game.throw(0)
        game.throw(2)
        for _ in range(15):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 15)
        """
            Testing different scored frames
        """

    def test_for_spare(self):
        game = BowlingGame()
        game.throw(4)
        game.throw(6)
        game.throw(7)
        game.throw(0)
        for _ in range(16):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 24)
        """
            Testing score for spares
        """

    def test_for_strike(self):
        game=BowlingGame()
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 17,0)
        game.calculate_score()
        self.assertEqual(game.score, 22)
        """
            Testing score for strikes
        """

BowlingGameTests.__doc__ = "Tests for basic function"