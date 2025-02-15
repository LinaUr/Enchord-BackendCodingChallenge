from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Block:
    shape: List[int]
    width: int
    height: int

"""
Block coordinates are stored as integers for efficiency.
Blocks are stored as if they were at the far left of the grid.
"""
INT_BLOCKS: Dict[str, Block] = {
    'Q': Block(
        shape=[int('11', 2) << 8,    # 0b1100000000
               int('11', 2) << 8],   # 0b1100000000
        width=2,
        height=2
    ),
    'Z': Block(
        shape=[int('110', 2) << 7,   # 0b1100000000
               int('011', 2) << 7],  # 0b0110000000
        width=3,
        height=2
    ),
    
    'S': Block(
        shape=[int('011', 2) << 7,   # 0b0110000000
               int('110', 2) << 7],  # 0b1100000000
        width=3,
        height=2
    ),
    
    'T': Block(
        shape=[int('111', 2) << 7,   # 0b1110000000
               int('010', 2) << 7],  # 0b0100000000
        width=3,
        height=2
    ),
    
    'I': Block(
        shape=[int('1111', 2) << 6], # 0b1111000000
        width=4,
        height=1
    ),
    
    'L': Block(
        shape=[int('10', 2) << 8,    # 0b1000000000
               int('10', 2) << 8,    # 0b1000000000
               int('11', 2) << 8],   # 0b1100000000
        width=2,
        height=3
    ),
    
    'J': Block(
        shape=[int('01', 2) << 8,    # 0b0100000000
               int('01', 2) << 8,    # 0b0100000000
               int('11', 2) << 8],   # 0b1100000000
        width=2,
        height=3
    ),
}
