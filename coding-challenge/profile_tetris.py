from memory_profiler import profile
from memory_profiler import memory_usage
import time
from tetris import tetris
from tetris_grid_using_ints import TetrisGridUsingInts
from tetris_grid_using_lists import TetrisGridUsingLists
from blocks import BLOCK_USING_INTS, BLOCKS_USING_LISTS

def test_cases(grid_implementation, block_types):
    print(tetris(grid_implementation(), block_types, "Q0"))
    print(tetris(grid_implementation(), block_types, "L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7"))
    print(tetris(grid_implementation(), block_types, "I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3"))
    print(tetris(grid_implementation(), block_types, "I1,I1,I1,I1,I1,I1,I1,I1"))
    print(tetris(grid_implementation(), block_types, ",".join(["Q0"] * 300000)))

@profile
def tetris_using_lists():
    return test_cases(TetrisGridUsingLists, BLOCKS_USING_LISTS)

@profile
def tetris_using_ints():
    return test_cases(TetrisGridUsingInts, BLOCK_USING_INTS)

# def profile_tetris_using_lists():
#     start = time.time()
#     mem_usage = memory_usage()
#     end = time.time()
#     print(f"Memory Usage: {max(mem_usage)} MiB")
#     print(f"Execution Time: {end - start} seconds")

def profile_tetris():
    for implementation in [tetris_using_lists, tetris_using_ints]:
        print(f"Profiling {implementation.__name__}...")
        start = time.time()
        mem_usage = memory_usage(implementation())
        end = time.time()
        print(f"Memory Usage: {max(mem_usage)} MiB")
        print(f"Execution Time: {end - start} seconds")

if __name__ == "__main__":
    profile_tetris()
