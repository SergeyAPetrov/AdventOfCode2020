from day7 import parse_line, parse_input, solve1, solve2


def test_parse_line():
    parent_bag, child_bags = parse_line("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    assert parent_bag == "light red"
    assert child_bags[0][0] == "bright white"
    assert child_bags[0][1] == 1
    assert child_bags[1][0] == "muted yellow"
    assert child_bags[1][1] == 2


def test_parse_simple_line():
    parent_bag, child_bags = parse_line("bright white bags contain 1 shiny gold bag.")
    assert parent_bag == "bright white"
    assert child_bags[0][0] == "shiny gold"
    assert child_bags[0][1] == 1


def test_parse_no_other_bags_line():
    parent_bag, child_bags = parse_line("faded blue bags contain no other bags.")
    assert parent_bag == "faded blue"
    assert len(child_bags) == 0


def test_parse_input():
    graph = parse_input(simple_input.splitlines())
    graph.reverse()
    assert graph.bfs_linked_nodes("shiny gold") == {"shiny gold", "bright white", "muted yellow", "dark orange", "light red"}


def test_parse_input2():
    graph = parse_input(simple_input.splitlines())
    assert graph.bfs_subtree_weight("shiny gold") - 1 == 32


def test_solve1():
    with open("day7.txt") as f:
        assert solve1(f.read()) == 372


def test_solve2():
    with open("day7.txt") as f:
        assert solve2(f.read()) == 8015

simple_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
