from day10 import solve1, solve2, count_monotonous_intervals, parse_input


def test_solve1_simple_input():
    assert solve1(input) == 35
    assert solve1(input2) == 220


def test_solve2_simple_input():
    assert solve2(input) == 8
    assert solve2(input2) == 19208


def test_solve1():
    with open("day10.txt") as f:
        assert solve1(f.read()) == 2450


def test_count_monotonous_intervals():
    jolts = parse_input(input)
    assert count_monotonous_intervals(jolts) == [2, 4, 3, 2, 1]


def test_solve2():
    with open("day10.txt") as f:
        assert solve2(f.read()) == 32396521357312


input = """16
10
15
5
1
11
7
19
6
12
4"""

input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""