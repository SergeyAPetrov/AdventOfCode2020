from day11 import solve


def test_solve1_simple_input():
    assert solve(simple_input, 1) == 37


def test_solve1():
    with open("day11.txt") as f:
        assert solve(f.read(), 1) == 2361


def test_solve2_simple_input():
    assert solve(simple_input, 2) == 26


def test_solve2():
    with open("day11.txt") as f:
        assert solve(f.read(), 2) == 2119


simple_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""