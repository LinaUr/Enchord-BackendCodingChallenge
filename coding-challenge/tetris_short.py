import sys
from blocks import SHORT_BLOCKS
from tetris_grid_short import TetrisGridShort

def tetris_short(input_line: str) -> int:
    """
    Tetrises the input sequence of pieces.
    Returns the filled height of the grid.
    """

    if not input_line:
        # input line is empty, meaning no block placed
        return 0

    grid = TetrisGridShort()
    
    for block in input_line.split(','):
        block_type = block[0]
        left_most_col = int(block[1])
        grid.insert_piece_from_top(SHORT_BLOCKS[block_type], left_most_col)
    
    return grid.get_fill_height()

def main():
    try:
        for line in sys.stdin:
            result = tetris_short(line.strip())
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
            print(tetris_short(input_line))
        except EOFError:
            break


def test_cases():
    # print(tetris_short("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7"), 1)
    # tetris_short("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7")
    # tetris_short("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3")

    print("test cases")
    print(tetris_short("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7"))
    print(tetris_short("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3"))
    print(tetris_short(",".join(["Q0"] * 1000)))
    # assert tetris_short("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    # assert tetris_short(",".join(["Q0"] * 1000)) == 2000
    

if __name__ == "__main__":
    # main()
    # local_test()
    test_cases()
