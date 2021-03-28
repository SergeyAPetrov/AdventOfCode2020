from day6 import solve1, solve2, count_anyone_answers, count_everyone_answers


def test_anyone_count_answers():
    assert count_anyone_answers("abc") == 3
    assert count_anyone_answers("""a
b
c""") == 3
    assert count_anyone_answers("""ab
ac""") == 3


def test_solve1_example():
    assert solve1(test_input) == 11


def test_solve1():
    with open("input.txt") as f:
        assert solve1(f.read()) == 6885


def test_everyone_count_answers():
    assert count_everyone_answers("abc") == 3
    assert count_everyone_answers("""a
b
c""") == 0
    assert count_everyone_answers("""ab
ac""") == 1


def test_solve2_example():
    assert solve2(test_input) == 6


def test_solve2():
    with open("input.txt") as f:
        assert solve2(f.read()) == 3550


test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""