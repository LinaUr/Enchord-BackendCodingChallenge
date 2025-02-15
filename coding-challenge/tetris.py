import profile
import sys
from tetris_grid import TetrisGrid
from blocks import BLOCKS

def tetris(input_line: str) -> int:
    """
    Tetrises the input sequence of pieces.
    Returns the filled height of the grid.
    """

    # If the input line is empty (meaning no block placed), return 0.
    if not input_line:
        return 0

    grid = TetrisGrid()
    
    for block in input_line.split(','):
        block_type = block[0]
        left_most_col = int(block[1])
        grid.insert_piece_from_top(BLOCKS[block_type], left_most_col)   
    
    return grid.get_block_height()

def main():
    try:
        for line in sys.stdin:
            line = line.strip()
            result = tetris(line.strip())
            sys.stdout.write(str(result) + "\n")
    except EOFError:
        sys.stdout.write("EOF detected, exitting from program...")
        sys.exit(0)
    except Exception as e:
        # Under Windows, I couldn't find a way to detect EOFError.
        # So, I just catch all exceptions to exit somewhat gracefully.
        sys.stdout.write("Exception: " + str(e) + "\n")
        sys.stdout.write("Exitting from program...")
        sys.exit(0)

def local_test():
    while True:
        try:
            input_line = input()
            print(tetris(input_line))
        except EOFError:
            break

def test_cases():
    assert tetris("Q0") == 2
    assert tetris("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    assert tetris("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    assert tetris("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    assert tetris(",".join(["Q0"] * 1000)) == 2000

if __name__ == "__main__":
    # main()
    # local_test()
    test_cases()