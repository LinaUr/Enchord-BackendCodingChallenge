import sys
from blocks import INT_BLOCKS
from tetris_grid_int import TetrisGridInt


def tetris_int(input_line: str) -> int:
    """
    Tetrises the input sequence of pieces.
    Returns the filled height of the grid.
    """

    if not input_line:
        # input line is empty, meaning no block placed
        return 0

    grid = TetrisGridInt()
    
    for block in input_line.split(','):
        block_type, left_most_col = block
        grid.insert_piece_from_top(INT_BLOCKS[block_type], left_most_col)
    
    return grid.get_fill_height()

def main():
    try:
        for line in sys.stdin:
            result = tetris_int(line.strip())
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
            print(tetris_int(input_line))
        except EOFError:
            break

def test_cases():
    print(tetris_int("J0,J1,J2,J3"), 16)

if __name__ == "__main__":
    main()
    # local_test()
    # test_cases()