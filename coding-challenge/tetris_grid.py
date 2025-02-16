from abc import ABC,abstractmethod
from blocks import BlockType

class TetrisGrid(ABC):
    """
    Abstract base class for Tetris grids.
    """

    @abstractmethod
    def get_fill_height(self) -> int:
        pass

    @abstractmethod
    def insert_block_from_top(self, block: BlockType, left_most_col: int) -> None:
        pass
