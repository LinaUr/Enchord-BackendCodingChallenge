
from unittest import TestCase
from tetris_grid_using_lists import TetrisGridUsingLists
from tetris_grid_using_ints import TetrisGridUsingInts
from blocks import BLOCKS_USING_LISTS, BLOCK_USING_INTS
from tetris import tetris

class TetrisTest(TestCase):
    """
    Tests for the tetris function.
    """

    def setUp(self):
        self.implementations = [
            (TetrisGridUsingLists, dict(BLOCKS_USING_LISTS)), # Create copy of dict to avoid modifying original
            (TetrisGridUsingInts, dict(BLOCK_USING_INTS)),
        ]

    def test_tetris_simple_input(self):
        print("Starting simple input test...", [blocks.keys() for _, blocks in self.implementations], flush=True)
        for grid_implementation, block_types in self.implementations:
            with self.subTest(grid=grid_implementation, block_types=block_types):
                self.assertEqual(tetris(grid_implementation(), block_types, "Q0"), 2)
                self.assertEqual(tetris(grid_implementation(), block_types, ",".join(["Q0"] * 50)), 100)
                self.assertEqual(tetris(grid_implementation(), block_types, "I0,J0,L0"), 7)
                self.assertEqual(tetris(grid_implementation(), block_types, "T0,T1,T2,T3"), 8)
                self.assertEqual(tetris(grid_implementation(), block_types, "L0,J0,I0"), 7)
                self.assertEqual(tetris(grid_implementation(), block_types, "S0,Z0,T0,I0"), 7)
                self.assertEqual(tetris(grid_implementation(), block_types, "I1,I1,I1,I1,I1,I1,I1,I1"), 8)
                self.assertEqual(tetris(grid_implementation(), block_types, "L0,L1,L2,L3"), 6)
                self.assertEqual(tetris(grid_implementation(), block_types, "J0,J1,J2,J3"), 12)
                self.assertEqual(tetris(grid_implementation(), block_types, "Q0,I0,L0,J0,S0,T0,Z0"), 15)


    def test_tetris_includes_removals(self):
        for grid_implementation, block_types in self.implementations:
            with self.subTest(grid=grid_implementation, block_types=block_types):
                self.assertEqual(tetris(grid_implementation(), block_types, "L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7"), 1)
                self.assertEqual(tetris(grid_implementation(), block_types, "I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3"), 8)


    def test_tetris_zigzag_blocks(self):
        for grid_implementation, block_types in self.implementations:
            with self.subTest(grid=grid_implementation, block_types=block_types):
                self.assertEqual(tetris(grid_implementation(), block_types, ",".join(["S0,Z1"] * 1000)), 4000)
                self.assertEqual(tetris(grid_implementation(), block_types, ",".join(["S0,Z2"] * 1000)), 2001)


    def test_tetris_large_input(self):
        for grid_implementation, block_types in self.implementations:
            with self.subTest(grid=grid_implementation, block_types=block_types):
                self.assertEqual(tetris(grid_implementation(), block_types, ",".join(["Q0"] * 300000)), 600000)
                # self.assertEqual(tetris(grid_implementation(), block_types, ",".join(["Q0"] * 1000000)), 2000000)
