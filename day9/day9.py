from collections import deque


def is_valid_number(deque, number):
    diffs = [abs(x - number) for x in deque]
    return any(diff in deque for diff in diffs)


def find_invalid_number(numbers, window_size=25):
    d = deque(numbers[:window_size])
    for number in numbers[window_size:]:
        if not is_valid_number(d, number):
            return number
        d.popleft()
        d.append(number)


def find_weakness(numbers, target):
    start, end = 0, 1
    while end < len(numbers):
        candidate = sum(numbers[start:end])
        if candidate == target:
            return min(numbers[start:end]) + max(numbers[start:end])
        if candidate < target:
            end += 1
        if candidate > target:
            start += 1


def solve1(input):
    numbers = [int(number) for number in input.splitlines()]
    return find_invalid_number(numbers)


def solve2(input):
    numbers = [int(number) for number in input.splitlines()]
    target = find_invalid_number(numbers)
    return find_weakness(numbers, target)
