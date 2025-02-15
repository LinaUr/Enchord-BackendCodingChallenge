from typing import List, Tuple

from numpy import ubyte, ushort
from blocks import ShortBlock

class TetrisGridShort:
    grid: List[ushort]

    _full_row: ushort
    _width: ubyte
    _bitmask_by_column: List[ushort]
    _fill_height_by_column: List[int]

    def __init__(self):
        self.grid = [ushort(0)]

        self._full_row = ushort(int('1111111111', 2))
        self._width = ubyte(10)
        self._bitmask_by_column = [ushort(int('1000000000', 2)) >> i for i in range(self._width)]
        self._fill_height_by_column = [0] * self._width
        

    def get_fill_height(self) -> int:
        return max(self._fill_height_by_column)
    

    def insert_piece_from_top(self, block: ShortBlock, left_most_col: int) -> None:
        while self._get_height() < block.height:
            # grid not height enough
            self._insert_row_at_top()

        # Check each column the block would occupy has enough space
        for col_offset in range(block.width):
            grid_col = left_most_col + col_offset
            if self._fill_height_by_column[grid_col] > self._get_height() - block.height:
                # At least one column is too full to fit the block
                self._insert_row_at_top()

        # Find highest fill height among columns the block will occupy
        max_fill_height = max(self._fill_height_by_column[left_most_col:left_most_col + block.width])
        
        # Start checking from the row that's block.height above the highest fill the block will cover
        grid_row = max(0, self._get_height() - max_fill_height - block.height) # Ensure we don't start below grid bottom
        valid_placement_at = None

        while True:
            if self._is_valid_block_placement((grid_row, left_most_col), block):
                valid_placement_at = (grid_row, left_most_col)
                # move piece down and check again
                grid_row += 1
                continue
            elif grid_row == 0:
                # extend grid and try again (ala move piece up)
                self._insert_row_at_top()
                self.insert_piece_from_top(block, left_most_col)
                return 
            else:
                # piece didn't fit, but we had already moved it down and thus found a valid placement before
                break

        if valid_placement_at:
            self._insert_block(valid_placement_at, block)
            bottom_row_idx = valid_placement_at[0] + block.height - 1
            rows_removed = self._remove_full_rows(bottom_row_idx, block.height)
            if rows_removed > 0:
                self._update_fill_heights(bottom_row_idx, rows_removed)


    def _insert_block(self, top_left_corner_in_grid: Tuple[int, int], block: ShortBlock):
        grid_row_idx, grid_col_idx = top_left_corner_in_grid
        for block_row in block.coverage:
            # move block n columns to the right into the grid,
            # then store bitwise OR with the grid row into the grid
            block_row_shifted = block_row >> grid_col_idx
            self.grid[grid_row_idx] |= block_row_shifted

            # Update fill height for each column affected by this block row
            for col_offset in range(block.width):
                col_idx = grid_col_idx + col_offset
                # Check if this block row has a '1' in this column
                if (block_row_shifted & self._bitmask_by_column[col_idx]) != 0:
                    # Update max height for this column if current row is higher
                    self._fill_height_by_column[col_idx] = max(
                        self._fill_height_by_column[col_idx],
                        self._get_height() - grid_row_idx
                    )

            grid_row_idx += 1
    

    def _get_height(self) -> int:
        return len(self.grid)
    

    def _insert_row_at_top(self) -> None:
        self.grid.insert(0, ushort(0))


    def _remove_full_rows(self, bottom_grid_row: int, height_of_block: int) -> int:
        rows_removed = 0
        for row_idx in range(bottom_grid_row, bottom_grid_row - height_of_block, -1):
            if self.grid[row_idx] == self._full_row:
                self.grid.pop(row_idx)
                rows_removed += 1

        return rows_removed


    def _update_fill_heights(self, bottom_grid_row: int, rows_removed: int) -> None:
        self._fill_height_by_column = [
            height - rows_removed if height > (self._get_height() - bottom_grid_row) else height 
            for height in self._fill_height_by_column
        ]


    def _is_valid_block_placement(self, top_left_corner_in_grid: Tuple[int, int], block: ShortBlock) -> bool:
        grid_row_idx, grid_col_idx = top_left_corner_in_grid
        for block_row in block.coverage:
            if grid_row_idx >= len(self.grid):
                # block is trying to be placed (partially) out of bounds
                return False
            
            # move block n columns to the right into the grid,
            # then do a bitwise AND with the grid row
            if self.grid[grid_row_idx] & (block_row >> grid_col_idx) != 0:
                # there is a collision of pieces when trying to place the block
                return False
            
            grid_row_idx += 1
        return True