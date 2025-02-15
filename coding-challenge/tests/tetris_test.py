
from unittest import TestCase
from tetris_int import tetris_int

class TetrisTest(TestCase):
    def test_tetris_int(self):
        self.assertEqual(tetris_int("Q0"), 2)
        self.assertEqual(tetris_int(",".join(["Q0"] * 50)), 100)

        self.assertEqual(tetris_int("I0,J0,L0"), 7)
        self.assertEqual(tetris_int("T0,T1,T2,T3"), 8)
        self.assertEqual(tetris_int("L0,J0,I0"), 7)
        self.assertEqual(tetris_int("S0,Z0,T0,I0"), 7)
        self.assertEqual(tetris_int("I1,I1,I1,I1,I1,I1,I1,I1"), 8)
        self.assertEqual(tetris_int("L0,L1,L2,L3"), 6)
        self.assertEqual(tetris_int("J0,J1,J2,J3"), 12)
        self.assertEqual(tetris_int("Q0,I0,L0,J0,S0,T0,Z0"), 15)


    # def test_tetris_int_includes_removals(self):
    #     self.assertEqual(tetris_int("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7"), 1)
    #     self.assertEqual(tetris_int("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3"), 8)

    # def test_tetris_int_large_input(self):
    #     # Test with very large number of pieces
    #     large_input = ",".join(["Q0"] * 1000000)
    #     self.assertEqual(tetris_int(large_input), 2000000)

    # def test_tetris_int_alternating_pieces(self):
    #     # Test with alternating pieces that could cause many row checks
    #     alternating = ",".join(["I0,Q1,I2,Q3"] * 50000) 
    #     self.assertEqual(tetris_int(alternating), 100000)

    # def test_tetris_int_zigzag_pieces(self):
    #     # Test with pieces that create many gaps and require lots of collision checks
    #     zigzag = ",".join(["S0,Z1"] * 100000)
    #     self.assertEqual(tetris_int(zigzag), 200000)

    # def test_tetris_int_tall_pieces(self):
    #     # Test with pieces that require extending grid height frequently
    #     tall_pieces = ",".join(["I0"] * 200000) 
    #     self.assertEqual(tetris_int(tall_pieces), 200000)

    
