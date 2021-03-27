from day5 import Seat, solve1, solve2


def test_seat_constructor():
    assert Seat("FBFBBFFRLR").seat_id() == 357
    assert Seat("BFFFBBFRRR").seat_id() == 567
    assert Seat("FFFBBBFRRR").seat_id() == 119
    assert Seat("BBFFBBFRLL").seat_id() == 820


def test_solve1():
    with open("input.txt") as f:
        assert solve1(f.read()) == 919


def test_solve2():
    with open("input.txt") as f:
        assert solve2(f.read()) == 642
