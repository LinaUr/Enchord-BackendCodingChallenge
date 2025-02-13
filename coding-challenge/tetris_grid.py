from typing import List, Tuple

class TetrisGrid:
    _WIDTH = 10

    def __init__(self):
        self.grid = [[0] * self._WIDTH]
    
    def get_block_height(self) -> int:
        if len(self.grid) == 0:
            return 0
        while sum(self.grid[0]) == 0:
            self.grid.pop(0)

        return len(self.grid)
    
    def insert_piece_from_top(self, block_coords: List[List[bool]], left_most_col: int) -> None:
        while self._get_height() < len(block_coords):
            self._insert_row_at_top()

        grid_row = 0
        grid_col = left_most_col

        valid_placement_at = None

        while True:
            if self._is_valid_block_placement(block_coords, (grid_row, grid_col)):
                valid_placement_at = (grid_row, grid_col)
                # move piece down and check again
                grid_row += 1
                continue
            elif grid_row == 0:
                # extend grid and try again (ala move piece up)
                self._insert_row_at_top()
                self.insert_piece_from_top(block_coords, left_most_col)
                return 
            else:
                # piece didn't fit, but we had already moved it down and thus found a valid placement before
                break

        if valid_placement_at:
            self._insert_block(valid_placement_at, block_coords)

    def _insert_block(self, top_left_grid_coord: Tuple[int, int], block_coords: List[List[bool]]):
        for block_row_idx in range(len(block_coords)):
            for block_col_idx in range(len(block_coords[block_row_idx])):
                if block_coords[block_row_idx][block_col_idx]:
                    self.grid[top_left_grid_coord[0] + block_row_idx][top_left_grid_coord[1] + block_col_idx] = 1
        self._remove_full_rows(top_left_grid_coord[0], len(block_coords))
    
    def _get_height(self) -> int:
        return len(self.grid)
    
    def _insert_row_at_top(self) -> None:
        self.grid.insert(0, [0] * self._WIDTH)

    def _remove_full_rows(self, top_row: int, height: int) -> None:
        for row in range(top_row + height-1, top_row-1, -1):
            if sum(self.grid[row]) == self._WIDTH:
                self.grid.pop(row)

    def _is_valid_block_placement(self, block_coords: List[List[bool]], top_left_grid_coord: Tuple[int, int]) -> bool:
        grid_height = self._get_height()
        grid_width = self._WIDTH
        for block_row_idx in range(len(block_coords)):
            for block_col_idx in range(len(block_coords[block_row_idx])):
                if top_left_grid_coord[0] + block_row_idx >= grid_height or top_left_grid_coord[1] + block_col_idx >= grid_width:
                    # piece is out of bounds
                    return False
                
                is_grid_field_occupied = self.grid[top_left_grid_coord[0] + block_row_idx][top_left_grid_coord[1] + block_col_idx]
                is_block_field_occupied = block_coords[block_row_idx][block_col_idx]
                if is_grid_field_occupied and is_block_field_occupied:
                    # piece is overlapping with another piece
                    return False
        return True