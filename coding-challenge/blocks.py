from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class IntBlock:
    coverage: List[int]
    width: int
    height: int

"""
Block coverage is stored as integers for memory and runtime efficiency.
Blocks are stored in binary format as if they were placed at the far left of the grid.
"""
BLOCK_USING_INTS: Dict[str, IntBlock] = {
    'Q': IntBlock(
        coverage=[int('11', 2) << 8,    # 0b1100000000
                  int('11', 2) << 8],   # 0b1100000000
        width=2,
        height=2
    ),
    'Z': IntBlock(
        coverage=[int('110', 2) << 7,   # 0b1100000000
                  int('011', 2) << 7],  # 0b0110000000
        width=3,
        height=2
    ),
    
    'S': IntBlock(
        coverage=[int('011', 2) << 7,   # 0b0110000000
                  int('110', 2) << 7],  # 0b1100000000
        width=3,
        height=2
    ),
    
    'T': IntBlock(
        coverage=[int('111', 2) << 7,   # 0b1110000000
                  int('010', 2) << 7],  # 0b0100000000
        width=3,
        height=2
    ),
    
    'I': IntBlock(
        coverage=[int('1111', 2) << 6], # 0b1111000000
        width=4,
        height=1
    ),
    
    'L': IntBlock(
        coverage=[int('10', 2) << 8,    # 0b1000000000
                  int('10', 2) << 8,    # 0b1000000000
                  int('11', 2) << 8],   # 0b1100000000
        width=2,
        height=3
    ),
    
    'J': IntBlock(
        coverage=[int('01', 2) << 8,    # 0b0100000000
                  int('01', 2) << 8,    # 0b0100000000
                  int('11', 2) << 8],   # 0b1100000000
        width=2,
        height=3
    ),
}


@dataclass
class ListBlock:
    coverage: List[List[bool]]
    width: int
    height: int

"""
Block coverage is stored as lists of lists of booleans for readability.
"""
BLOCKS_USING_LISTS: Dict[str, ListBlock] = {
    'Q': ListBlock(
        coverage=[
            [1, 1],
            [1, 1]
        ],
        width=2,
        height=2
    ),
    'Z': ListBlock(
        coverage=[
            [1, 1, 0],
            [0, 1, 1]
        ],
        width=3,
        height=2
    ),
    
    'S': ListBlock(
        coverage=[
            [0, 1, 1],
            [1, 1, 0]
        ],
        width=3,
        height=2
    ),
    
    'T': ListBlock(
        coverage=[
            [1, 1, 1],
            [0, 1, 0]
        ],
        width=3,
        height=2
    ),
    
    'I': ListBlock(
        coverage=[
            [1, 1, 1, 1]
        ],
        width=4,
        height=1
    ),
    
    'L': ListBlock(
        coverage=[
            [1, 0],
            [1, 0],
            [1, 1]
        ],
        width=2,
        height=3
    ),
    
    'J': ListBlock(
        coverage=[
            [0, 1],
            [0, 1],
            [1, 1]
        ],
        width=2,
        height=3
    ),
}


BlockType = Union[IntBlock, ListBlock]