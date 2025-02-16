import sys
from typing import Dict
from blocks import BLOCK_USING_INTS, BlockType
from tetris_grid import TetrisGrid
from tetris_grid_using_ints import TetrisGridUsingInts

def tetris(grid: TetrisGrid, block_types: Dict[str, BlockType], input_line: str) -> int:
    """
    Tetrises the input sequence of pieces.
    Returns the filled height of the grid.
    """

    if not input_line:
        # input line is empty, meaning no block placed
        return 0

    for block in input_line.split(','):
        block_type = block[0]
        left_most_col = int(block[1])        
        grid.insert_block_from_top(block_types[block_type], left_most_col)
    
    return grid.get_fill_height()


def main():
    # Change these two lines to switch between the two grid implementations
    grid, block_types = TetrisGridUsingInts(), BLOCK_USING_INTS
    
    try:
        for line in sys.stdin:
            result = tetris(grid, block_types, line.strip())
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


if __name__ == "__main__":
    main()
