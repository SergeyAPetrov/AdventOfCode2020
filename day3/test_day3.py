import day3

def test_get_collision_simple():
    assert day3.get_collision('.#....#..#.', 6) == 1

def test_get_collision_bigger_index():
    assert day3.get_collision('.#...##..#.', 12) == 1

def test_get_collision_bigger_index_no_collision():
    assert day3.get_collision('.#...##..#.', 11) == 0

def test_count_collisions():
    assert day3.count_collisions(simple_input.split(), di=1, dl=1) == 2
    assert day3.count_collisions(simple_input.split(), di=1, dl=3) == 7
    assert day3.count_collisions(simple_input.split(), di=1, dl=5) == 3
    assert day3.count_collisions(simple_input.split(), di=1, dl=7) == 4
    assert day3.count_collisions(simple_input.split(), di=2, dl=1) == 2

def test_count_multiple_collisions():
    assert day3.count_multiple_collisions(simple_input.split()) == 336

def test_solve1():
    with open('day3/input.txt') as f:
        assert day3.count_collisions(f.read().splitlines(), di=1, dl=3) == 195

def test_solve2():
    with open('day3/input.txt') as f:
        assert day3.count_multiple_collisions(f.read().splitlines()) == 3772314000

simple_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""