from day9 import is_valid_number, find_invalid_number, solve1, find_weakness, solve2
from collections import deque


def test_is_valid_number():
    d = deque([35, 20, 15, 25, 47])
    assert is_valid_number(d, 40)
    d.popleft()
    d.append(40)
    assert is_valid_number(d, 62)


def test_is_valid_number_invalid():
    d = deque([95, 102, 117, 150, 182])
    assert is_valid_number(d, 127) is False


def test_find_invalid_number():
    assert find_invalid_number(input, 5) == 127


def test_find_weakness():
    target = find_invalid_number(input, 5)
    assert find_weakness(input, target) == 62


def test_solve1():
    with open("day9.txt") as f:
        assert solve1(f.read()) == 248131121


def test_solve2():
    with open("day9.txt") as f:
        assert solve2(f.read()) == 31580383


input = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

