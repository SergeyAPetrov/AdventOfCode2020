def count_anyone_answers(one_group_input):
    return len(set(one_group_input.replace("\n", "")))


def count_everyone_answers(one_group_input):
    person_answers = [set(line) for line in one_group_input.split()]
    return len(set.intersection(*person_answers))


def solve1(input):
    return solver(input, count_anyone_answers)


def solve2(input):
    return solver(input, count_everyone_answers)


def solver(input, solve_func):
    return sum(solve_func(lines) for lines in input.split('\n\n'))
