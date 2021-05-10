from typing import List
from functools import reduce
from enum import Enum

empty_seat = "L"
floor = "."
taken_seat = "#"

Seats = List[List[str]]


class Direction(Enum):
    UP = 1
    RIGHT_UP = 2
    RIGHT = 3
    RIGHT_DOWN = 4
    DOWN = 5
    LEFT_DOWN = 6
    LEFT = 7
    LEFT_UP = 8


def parse_input(content):
    return content.splitlines()


def count_taken_visible_seats(seats: Seats, x, y, part):
    result = 0
    for direction in Direction:
        if is_taken_seat_in_direction(seats, x, y, direction, part):
            result += 1
    return result


def is_taken_seat_in_direction(seats: Seats, x, y, direction, part):
    width = len(seats[0])
    height = len(seats)
    while True:
        x, y = coordinate_direction_change(x, y, direction)
        if not(0 <= x < width and 0 <= y < height) or seats[y][x] == empty_seat:
            return False
        if seats[y][x] == taken_seat:
            return True
        if part == 1:
            return False


def coordinate_direction_change(x, y, direction):
    if direction is Direction.UP:
        return x, y-1
    if direction is Direction.RIGHT_UP:
        return x+1, y-1
    if direction is Direction.RIGHT:
        return x+1, y
    if direction is Direction.RIGHT_DOWN:
        return x+1, y+1
    if direction is Direction.DOWN:
        return x, y+1
    if direction is Direction.LEFT_DOWN:
        return x-1, y+1
    if direction is Direction.LEFT:
        return x-1, y
    if direction is Direction.LEFT_UP:
        return x-1, y-1


def should_be_taken(seats: Seats, x, y, part):
    return count_taken_visible_seats(seats, x, y, part) == 0


def should_be_freedup(seats: Seats, x, y, part):
    limit = 4 if part == 1 else 5
    return count_taken_visible_seats(seats, x, y, part) >= limit


def get_new_seat_state(seats: Seats, x, y, part):
    current_state = seats[y][x]
    if current_state == empty_seat and should_be_taken(seats, x, y, part):
        return taken_seat
    if current_state == taken_seat and should_be_freedup(seats, x, y, part):
        return empty_seat
    return current_state


def iterate_seats(seats: Seats, part):
    width = len(seats[0])
    height = len(seats)
    return [[get_new_seat_state(seats, x, y, part) for x in range(width)] for y in range(height)]


def count_taken_seats(seats: Seats):
    one_line = reduce(lambda x, y: x + y, seats)
    return len([seat for seat in one_line if seat == taken_seat])


def solve(content, part):
    seats = parse_input(content)
    previous_seats = []
    while seats != previous_seats:
        seats, previous_seats = iterate_seats(seats, part), seats
    return count_taken_seats(seats)
