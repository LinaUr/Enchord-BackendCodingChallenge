from memory_profiler import profile
from memory_profiler import memory_usage
import time
from tetris import tetris
from tetris_int import tetris_int
from tetris_short import tetris_short

@profile
def test_cases_tetris():
    assert tetris("Q0") == 2
    assert tetris("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    assert tetris("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    assert tetris("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    # assert tetris(",".join(["Q0"] * 1000)) == 2000
    # assert tetris(",".join(["Q0"] * 10000)) == 20000
    assert tetris(",".join(["Q0"] * 300000)) == 600000
    # assert tetris(",".join(["Q0"] * 1000000)) == 2000000

def profile_tetris():
    start = time.time()
    mem_usage = memory_usage(test_cases_tetris)
    end = time.time()

    print(f"Memory Usage: {max(mem_usage)} MiB")
    print(f"Execution Time: {end - start} seconds")


@profile
def test_cases_tetris_int():
    assert tetris_int("Q0") == 2
    assert tetris_int("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    assert tetris_int("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    assert tetris_int("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    # assert tetris_int(",".join(["Q0"] * 1000)) == 2000
    # assert tetris_int(",".join(["Q0"] * 10000)) == 20000
    assert tetris_int(",".join(["Q0"] * 300000)) == 600000
    # assert tetris_int(",".join(["Q0"] * 1000000)) == 2000000

def profile_tetris_int():
    start = time.time()
    mem_usage = memory_usage(test_cases_tetris_int)
    end = time.time()

    print(f"Memory Usage: {max(mem_usage)} MiB")
    print(f"Execution Time: {end - start} seconds")


@profile
def test_cases_tetris_short():
    assert tetris_short("Q0") == 2
    assert tetris_short("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    assert tetris_short("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    assert tetris_short("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    # assert tetris_short(",".join(["Q0"] * 1000)) == 2000
    # assert tetris_short(",".join(["Q0"] * 10000)) == 20000
    assert tetris_short(",".join(["Q0"] * 300000)) == 600000
    # assert tetris_short(",".join(["Q0"] * 1000000)) == 2000000

def profile_tetris_short():
    start = time.time()
    mem_usage = memory_usage(test_cases_tetris_short)
    end = time.time()

    print(f"Memory Usage: {max(mem_usage)} MiB")
    print(f"Execution Time: {end - start} seconds")

if __name__ == "__main__":
    profile_tetris()
    profile_tetris_int()
    profile_tetris_short()
