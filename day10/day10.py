import math


def solve1(input):
    jolts = parse_input(input)
    jolts.append(max(jolts) + 3)

    one_jolt_diff, three_jolt_diff = 0, 0
    for j1, j2 in zip(jolts, jolts[1:]):
        if j2 - j1 == 1:
            one_jolt_diff += 1
        elif j2 - j1 == 3:
            three_jolt_diff += 1
    return one_jolt_diff*three_jolt_diff


def parse_input(input):
    jolts = [int(jolt) for jolt in input.splitlines()]
    jolts.sort()
    jolts.insert(0, 0)

    return jolts


def solve2(input):
    jolts = parse_input(input)
    intervals = count_monotonous_intervals(jolts)
    return math.prod(interval_combinations(interval) for interval in intervals)


def count_monotonous_intervals(jolts):
    interval_sizes = []
    current_interval_length, previous_element = 1, jolts[0]
    for i, element in enumerate(jolts[1:]):
        if element - previous_element == 1:
            current_interval_length += 1
        else:
            interval_sizes.append(current_interval_length)
            current_interval_length = 1
        previous_element = element
    interval_sizes.append(current_interval_length)
    return interval_sizes


def interval_combinations(n):
    if n < 3:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    return 2*interval_combinations(n-1) - 1


