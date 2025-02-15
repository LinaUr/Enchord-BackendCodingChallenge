from dataclasses import dataclass
from typing import Dict, List
from numpy import ubyte, ushort

@dataclass
class ShortBlock:
    coverage: List[ushort]
    width: ubyte
    height: ubyte

"""
Block coordinates are stored as integers for efficiency.
Blocks are stored as if they were at the far left of the grid.
"""
SHORT_BLOCKS: Dict[str, ShortBlock] = {
    'Q': ShortBlock(
        coverage=[ushort(int('11', 2)) << 8,    # 0b1100000000
                  ushort(int('11', 2)) << 8],   # 0b1100000000
        width=2,
        height=2
    ),
    'Z': ShortBlock(
        coverage=[ushort(int('110', 2)) << 7,   # 0b1100000000
                  ushort(int('011', 2)) << 7],  # 0b0110000000
        width=3,
        height=2
    ),
    
    'S': ShortBlock(
        coverage=[ushort(int('011', 2)) << 7,   # 0b0110000000
                  ushort(int('110', 2)) << 7],  # 0b1100000000
        width=3,
        height=2
    ),
    
    'T': ShortBlock(
        coverage=[ushort(int('111', 2)) << 7,   # 0b1110000000
                  ushort(int('010', 2)) << 7],  # 0b0100000000
        width=3,
        height=2
    ),
    
    'I': ShortBlock(
        coverage=[ushort(int('1111', 2)) << 6], # 0b1111000000
        width=4,
        height=1
    ),
    
    'L': ShortBlock(
        coverage=[ushort(int('10', 2)) << 8,    # 0b1000000000
                  ushort(int('10', 2)) << 8,    # 0b1000000000
                  ushort(int('11', 2)) << 8],   # 0b1100000000
        width=2,
        height=3
    ),
    
    'J': ShortBlock(
        coverage=[ushort(int('01', 2)) << 8,    # 0b0100000000
                  ushort(int('01', 2)) << 8,    # 0b0100000000
                  ushort(int('11', 2)) << 8],   # 0b1100000000
        width=2,
        height=3
    ),
}

@dataclass
class IntBlock:
    coverage: List[int]
    width: int
    height: int

"""
Block coordinates are stored as integers for efficiency.
Blocks are stored as if they were at the far left of the grid.
"""
INT_BLOCKS: Dict[str, IntBlock] = {
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
class Block:
    coverage: List[List[bool]]
    width: int
    height: int

"""
Block coordinates are stored as integers for efficiency.
Blocks are stored as if they were at the far left of the grid.
"""
BLOCKS: Dict[str, Block] = {
    'Q': Block(
        coverage=[
            [1, 1],
            [1, 1]
        ],
        width=2,
        height=2
    ),
    'Z': Block(
        coverage=[
            [1, 1, 0],
            [0, 1, 1]
        ],
        width=3,
        height=2
    ),
    
    'S': Block(
        coverage=[
            [0, 1, 1],
            [1, 1, 0]
        ],
        width=3,
        height=2
    ),
    
    'T': Block(
        coverage=[
            [1, 1, 1],
            [0, 1, 0]
        ],
        width=3,
        height=2
    ),
    
    'I': Block(
        coverage=[
            [1, 1, 1, 1]
        ],
        width=4,
        height=1
    ),
    
    'L': Block(
        coverage=[
            [1, 0],
            [1, 0],
            [1, 1]
        ],
        width=2,
        height=3
    ),
    
    'J': Block(
        coverage=[
            [0, 1],
            [0, 1],
            [1, 1]
        ],
        width=2,
        height=3
    ),
}
