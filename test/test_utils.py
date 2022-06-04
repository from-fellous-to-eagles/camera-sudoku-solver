import unittest
from src import solver

class BasicTestSuite(unittest.TestCase):

    def setUp(self):
        self.board =  [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ]

        self.upper_left_corner = [
            [0,0,0],
            [0,8,0],
            [6,0,2],
        ]

        self.upper_right_corner = [
            [2,0,0],
            [0,9,0],
            [5,0,0],
        ]

        self.bottom_left_corner = [
            [0,0,5],
            [0,9,0],
            [0,0,6],
        ]

        self.bottom_right_corner = [
            [6,0,3],
            [0,7,0],
            [0,0,0],
        ]

        self.upper_middle = [
            [0,0,0],
            [0,0,7],
            [0,0,0],
        ]

        self.col_0 = [0,0,6,0,0,0,0,0,0]

        self.valid_row = [1,2,3,4,5,6,7,8,9]
        self.wrong_row = [1,2,2,3,4,5,6,7,8]
        self.row_too_big = [1,1,2,2,3,3,4,4,5,5,6,7,8,9]
        self.row_negative = [-1,-2,3,4,5,6,8,9,7]
        self.non_num_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.valid_block = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]

        self.wrong_block = [
            [1,1,1],
            [2,2,2],
            [3,3,3]
        ]

    def test_valid_row(self):
        self.assertTrue(solver.valid_row(self.valid_row))
        self.assertFalse(solver.valid_row(self.wrong_row))
        self.assertFalse(solver.valid_row(self.row_too_big))
        self.assertFalse(solver.valid_row(self.row_negative))
        self.assertFalse(solver.valid_row(self.non_num_row))

    def test_valid_block(self):
        self.assertTrue(solver.valid_block(self.valid_block))
        self.assertFalse(solver.valid_block(self.wrong_block))

    def test_retrieve_block(self):
        self.assertEqual(solver.retrieve_block(self.board, 0, 0), self.upper_left_corner)
        self.assertEqual(solver.retrieve_block(self.board, 0, 8), self.upper_right_corner)
        self.assertEqual(solver.retrieve_block(self.board, 8, 0), self.bottom_left_corner)
        self.assertEqual(solver.retrieve_block(self.board, 8, 8), self.bottom_right_corner)
        self.assertEqual(solver.retrieve_block(self.board, 1, 4), self.upper_middle)

    def test_retrieve_column(self):
        self.assertEqual(solver.retrieve_column(self.board, 0), self.col_0)

    def test_contains_duplicate(self):
        self.assertFalse(solver.contains_duplicate(self.valid_row))
        self.assertTrue(solver.contains_duplicate(self.wrong_row))

        self.assertFalse(solver.contains_duplicate( solver.flattened_block(self.valid_block) ))
        self.assertFalse(solver.contains_duplicate( solver.flattened_block(self.valid_block) ))
