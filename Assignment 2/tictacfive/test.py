import unittest
import numpy as np
from heuristics import base_heuristic
from game_state import game_state


class TestHeuristic(unittest.TestCase):

    def run_test(self, grid, expected, description):
        # Create a game state from the grid and pass it to heuristic
        state = game_state(grid, 1, None, 0)  # Player 1 is the current player
        result = base_heuristic(state)
        self.assertEqual(result, expected, f"{description}: Expected {expected}, but got {result}")

    def test_1(self):
        grid = np.array([
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=1, description="Test 1: Player 1, 3-in-a-row with two open sides")

    def test_2(self):
        grid = np.array([
            [0, 2, 2, 2, 2],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=-1, description="Test 2: Player 2, 4-in-a-row with one open side")

    def test_3(self):
        grid = np.array([
            [0, 1, 1, 1, 0],
            [0, 2, 2, 2, 2],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 3: Mixed sequences for both players")

    def test_4(self):
        grid = np.array([
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 4: Boundary sequence for Player 1")

    def test_5(self):
        grid = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 5: Empty grid")

    def test_6(self):
        grid = np.array([
            [1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1]
        ])
        self.run_test(grid, expected=0, description="Test 6: No valid sequences")

    def test_7(self):
        grid = np.array([
            [1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 7: Player 1 has better sequence")

    def test_8(self):
        grid = np.array([
            [2, 0, 0, 0, 2],
            [1, 1, 1, 2, 0],
            [2, 1, 0, 2, 1],
            [1, 0, 1, 1, 0],
            [2, 0, 0, 0, 1]
        ])
        self.run_test(grid, expected=0, description="Test 8: Player 2 has better sequence")

    # New tests added here

    def test_9(self):
        grid = np.array([
            [1, 1, 1, 0, 0],
            [1, 2, 2, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 9: Player 2, multiple 3-in-a-row sequences")

    def test_10(self):
        grid = np.array([
            [2, 2, 2, 0, 0],
            [0, 2, 2, 0, 0],
            [0, 2, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 10: Player 2, 4-in-a-row and 3-in-a-row sequences")

    def test_11(self):
        grid = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 11: All spots empty")

    def test_12(self):
        grid = np.array([
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 12: Player 1 has no sequences yet")

    def test_13(self):
        grid = np.array([
            [2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.run_test(grid, expected=0, description="Test 13: Player 2 has no sequences yet")

    def test_14(self):
        grid = np.array([
            [1, 2, 0, 0, 0],
            [2, 1, 1, 0, 0],
            [0, 2, 2, 0, 0],
            [1, 2, 1, 2, 0],
            [1, 2, 1, 2, 2]
        ])
        self.run_test(grid, expected=0, description="Test 14: Complex mixed grid with no sequences")

    def test_15(self):
        grid = np.array([
            [1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 1],
            [1, 0, 1, 1, 1]
        ])
        self.run_test(grid, expected=1, description="Test 15: Player 1 has a 3-in-a-row and Player 2 does not")

if __name__ == "__main__":
    unittest.main()