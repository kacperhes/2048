import unittest
from unittest.mock import patch
from game import Game

class GameTest(unittest.TestCase):
    def __create_game(self):
        self.game = Game()


    def setUp(self) -> None:
        self.__create_game()


    def test_create_game(self):
        self.assertEqual(self.game.width, 4)
        self.assertEqual(self.game.height, 4)
        self.assertTrue(any(any(row) for row in self.game.grid)) # check if there're non 0 values


    @patch.object(Game, '_Game__spawn_random_number', return_value=None)
    def test_move_left(self, mock_spawn):
        self.game.grid = [
            [2,0,4,0],
            [2,2,2,2],
            [0,0,0,0],
            [2,2,4,4],
        ]
        expected = [
            [2,4,0,0],
            [4,4,0,0],
            [0,0,0,0],
            [4,8,0,0],
        ]
        self.game.make_move('LEFT')
        self.assertEqual(self.game.grid, expected)


    @patch.object(Game, '_Game__spawn_random_number', return_value=None)
    def test_move_right(self, mock_spawn):
        self.game.grid = [
            [0,4,0,2],
            [2,2,2,2],
            [0,0,0,0],
            [2,2,4,4],
        ]
        expected = [
            [0,0,4,2],
            [0,0,4,4],
            [0,0,0,0],
            [0,0,4,8],
        ]
        self.game.make_move('RIGHT')
        self.assertEqual(self.game.grid, expected)


    @patch.object(Game, '_Game__spawn_random_number', return_value=None)
    def test_move_up(self, mock_spawn):
        self.game.grid = [
            [2, 0, 2, 0],
            [2, 2, 0, 0],
            [0, 0, 2, 2],
            [2, 2, 4, 4],
        ]
        expected = [
            [4, 4, 4, 2],
            [2, 0, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.game.make_move('UP')
        self.assertEqual(self.game.grid, expected)

    @patch.object(Game, '_Game__spawn_random_number', return_value=None)
    def test_move_down(self, mock_spawn):
        self.game.grid = [
            [2, 0, 2, 2],
            [2, 2, 0, 2],
            [0, 0, 2, 2],
            [2, 2, 4, 2],
        ]
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 4, 4],
            [4, 4, 4, 4],
        ]
        self.game.make_move('DOWN')
        self.assertEqual(self.game.grid, expected)

    def test_accumulate_points(self):
        self.game.grid = [
            [2, 0, 2, 2],
            [2, 2, 0, 2],
            [0, 0, 2, 2],
            [2, 2, 4, 2],
        ]
        self.game.points = 0
        self.game.make_move('DOWN')
        self.assertEqual(self.game.points, 20) # 4 from first column + 4 from second + 4 from third + 8 (2 merges) from last

    def test_can_move(self):
        self.game.grid = [
            [2, 16, 2, 2],
            [2, 2, 8, 2],
            [2, 4, 2, 2],
            [2, 2, 4, 2],
        ]
        self.assertTrue(self.game.can_move())


    def test_cannot_move(self):
        self.game.grid = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [512, 1024, 2048, 4096],
            [8192, 16384, 32768, 65536],
        ]
        self.assertFalse(self.game.can_move())