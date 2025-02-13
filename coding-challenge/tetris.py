import sys
from typing import Dict, List
from tetris_grid import TetrisGrid

BLOCK_COORDS_BY_PIECE: Dict[str, List[List[bool]]] = {
    'Q': [[1,1],
          [1,1]],
    
    'Z': [[1,1,0],
          [0,1,1]],
    
    'S': [[0,1,1],
          [1,1,0]],
    
    'T': [[1,1,1],
          [0,1,0]],
    
    'I': [[1,1,1,1]],
    
    'L': [[1,0],
          [1,0],
          [1,1]],
    
    'J': [[0,1],
          [0,1],
          [1,1]],
}

def tetris(input_line: str) -> int:
    """
    Tetrises the input sequence of pieces.
    Returns the filled height of the grid.
    """
    grid = TetrisGrid()
    
    for piece in input_line.split(','):
        piece_type = piece[0]
        col = int(piece[1])
        grid.insert_piece_from_top(BLOCK_COORDS_BY_PIECE[piece_type], col)        
    
    return grid.get_block_height()

def main():
    input_line = sys.stdin.readline().strip()
    result = tetris(input_line)
    sys.stdout.write(str(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
