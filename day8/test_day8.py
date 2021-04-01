from day8 import solve1, solve2


def test_simple_solve1():
    assert solve1(simple_input) == 5


def test_simple_solve2():
    assert solve2(simple_input) == 8


def test_solve1():
    with open("day8.txt") as f:
        assert solve1(f.read()) == 2003


def test_solve2():
    with open("day8.txt") as f:
        assert solve2(f.read()) == 1984


simple_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

