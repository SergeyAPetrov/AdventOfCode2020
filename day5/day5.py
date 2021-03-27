class Seat:
    def __init__(self, line):
        self.row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        self.column = int(line[-3:].replace("L", "0").replace("R", "1"), 2)

    def seat_id(self):
        return self.row*8 + self.column


def solve1(input):
    seats = get_seats(input)
    return max(seats, key=lambda s: s.seat_id()).seat_id()


def solve2(input):
    seat_ids = [seat.seat_id() for seat in (get_seats(input))]

    min_seat, max_seat = min(seat_ids), max(seat_ids)
    answer = set(range(min_seat, max_seat)) - set(seat_ids)
    return next(iter(answer))

    # seat_ids.sort()
    # prev_seat = seat_ids[0]
    # for i in range(1, len(seat_ids)):
    #     if prev_seat + 2 == seat_ids[i]:
    #         return prev_seat + 1
    #     prev_seat = seat_ids[i]


def get_seats(input):
    return [Seat(line) for line in input.split()]
