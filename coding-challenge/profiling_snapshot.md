PS C:\Users\Lina\Desktop\Projects\Enchord> & c:/Users/Lina/Desktop/Projects/Enchord/coding-challenge/.venv/Scripts/python.exe c:/Users/Lina/Desktop/Projects/Enchord/coding-challenge/profile_tetris.py
Filename: c:\Users\Lina\Desktop\Projects\Enchord\coding-challenge\profile_tetris.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     8     32.6 MiB     32.6 MiB           1   @profile
     9                                         def test_cases_tetris():
    10     32.6 MiB      0.0 MiB           1       assert tetris("Q0") == 2
    11     32.6 MiB      0.0 MiB           1       assert tetris("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1      
    12     32.6 MiB      0.0 MiB           1       assert tetris("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    13     32.6 MiB      0.0 MiB           1       assert tetris("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    14                                             # assert tetris(",".join(["Q0"] * 1000)) == 2000
    15                                             # assert tetris(",".join(["Q0"] * 10000)) == 20000
    16     34.0 MiB      1.4 MiB           1       assert tetris(",".join(["Q0"] * 100000)) == 200000
    17                                             # assert tetris(",".join(["Q0"] * 1000000)) == 2000000


Memory Usage: 68.98046875 MiB
Execution Time: 24.04549765586853 seconds
Filename: c:\Users\Lina\Desktop\Projects\Enchord\coding-challenge\profile_tetris.py

=============================================================
    28     34.0 MiB     34.0 MiB           1   @profile
    29                                         def test_cases_tetris_int():
    30     34.0 MiB      0.0 MiB           1       assert tetris_int("Q0") == 2
    31     34.0 MiB      0.0 MiB           1       assert tetris_int("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    32     34.0 MiB      0.0 MiB           1       assert tetris_int("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    33     34.0 MiB      0.0 MiB           1       assert tetris_int("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    34                                             # assert tetris_int(",".join(["Q0"] * 1000)) == 2000
    35                                             # assert tetris_int(",".join(["Q0"] * 10000)) == 20000
    36     34.4 MiB      0.4 MiB           1       assert tetris_int(",".join(["Q0"] * 100000)) == 200000
    37                                             # assert tetris_int(",".join(["Q0"] * 1000000)) == 2000000


Memory Usage: 46.3046875 MiB
Execution Time: 19.73503613471985 seconds
Filename: c:\Users\Lina\Desktop\Projects\Enchord\coding-challenge\profile_tetris.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    48     34.5 MiB     34.5 MiB           1   @profile
    49                                         def test_cases_tetris_short():
    50     34.5 MiB      0.0 MiB           1       assert tetris_short("Q0") == 2
    51     34.5 MiB      0.0 MiB           1       assert tetris_short("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    52     34.5 MiB      0.0 MiB           1       assert tetris_short("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    53     34.5 MiB      0.0 MiB           1       assert tetris_short("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    54                                             # assert tetris_short(",".join(["Q0"] * 1000)) == 2000
    55                                             # assert tetris_short(",".join(["Q0"] * 10000)) == 20000
    56     34.4 MiB     -0.1 MiB           1       assert tetris_short(",".join(["Q0"] * 100000)) == 200000
    57                                             # assert tetris_short(",".join(["Q0"] * 1000000)) == 2000000


Memory Usage: 46.33984375 MiB
Execution Time: 20.394981145858765 seconds
PS C:\Users\Lina\Desktop\Projects\Enchord> & c:/Users/Lina/Desktop/Projects/Enchord/coding-challenge/.venv/Scripts/python.exe c:/Users/Lina/Desktop/Projects/Enchord/coding-challenge/profile_tetris.py
Filename: c:\Users\Lina\Desktop\Projects\Enchord\coding-challenge\profile_tetris.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     8     32.8 MiB     32.8 MiB           1   @profile
     9                                         def test_cases_tetris():
    10     32.8 MiB      0.0 MiB           1       assert tetris("Q0") == 2
    11     32.8 MiB      0.0 MiB           1       assert tetris("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    12     32.8 MiB      0.0 MiB           1       assert tetris("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    13     32.8 MiB      0.0 MiB           1       assert tetris("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    14                                             # assert tetris(",".join(["Q0"] * 1000)) == 2000
    15                                             # assert tetris(",".join(["Q0"] * 10000)) == 20000
    16     34.3 MiB      1.5 MiB           1       assert tetris(",".join(["Q0"] * 300000)) == 600000
    17                                             # assert tetris(",".join(["Q0"] * 1000000)) == 2000000


Memory Usage: 137.25390625 MiB
Execution Time: 120.22652816772461 seconds
Filename: c:\Users\Lina\Desktop\Projects\Enchord\coding-challenge\profile_tetris.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    28     34.3 MiB     34.3 MiB           1   @profile
    29                                         def test_cases_tetris_int():
    30     34.3 MiB      0.0 MiB           1       assert tetris_int("Q0") == 2
    31     34.3 MiB      0.0 MiB           1       assert tetris_int("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    32     34.3 MiB      0.0 MiB           1       assert tetris_int("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    33     34.3 MiB      0.0 MiB           1       assert tetris_int("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    34                                             # assert tetris_int(",".join(["Q0"] * 1000)) == 2000
    35                                             # assert tetris_int(",".join(["Q0"] * 10000)) == 20000
    36     34.2 MiB     -0.1 MiB           1       assert tetris_int(",".join(["Q0"] * 300000)) == 600000
    37                                             # assert tetris_int(",".join(["Q0"] * 1000000)) == 2000000


Memory Usage: 73.046875 MiB
Execution Time: 107.07096791267395 seconds
Filename: c:\Users\Lina\Desktop\Projects\Enchord\coding-challenge\profile_tetris.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    48     34.3 MiB     34.3 MiB           1   @profile
    49                                         def test_cases_tetris_short():
    50     34.3 MiB      0.0 MiB           1       assert tetris_short("Q0") == 2
    51     34.3 MiB      0.0 MiB           1       assert tetris_short("L0,I3,J8,T6,T1,Q4,Z5,S2,I0,I6,Q4,T0,T7") == 1
    52     34.3 MiB      0.0 MiB           1       assert tetris_short("I2,S0,Q3,I5,J8,S2,T6,S4,S7,J0,T1,J8,T6,I0,T3") == 8
    53     34.3 MiB      0.0 MiB           1       assert tetris_short("I1,I1,I1,I1,I1,I1,I1,I1") == 8
    54                                             # assert tetris_short(",".join(["Q0"] * 1000)) == 2000
    55                                             # assert tetris_short(",".join(["Q0"] * 10000)) == 20000
    56     34.4 MiB      0.1 MiB           1       assert tetris_short(",".join(["Q0"] * 300000)) == 600000
    57                                             # assert tetris_short(",".join(["Q0"] * 1000000)) == 2000000


Memory Usage: 73.12890625 MiB
Execution Time: 107.18750190734863 seconds
PS C:\Users\Lina\Desktop\Projects\Enchord> 