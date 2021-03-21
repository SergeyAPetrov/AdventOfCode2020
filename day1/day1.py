import itertools

def parse(input):
    return [int(row) for row in input.split()]

def solve1(entries):
    first, second = [(a,b) for a in entries for b in entries if a+b == 2020][0]
    return first * second
    
def solve2(entries):
    first, second, third = [(a,b,c) for (a,b,c) in itertools.product(entries, repeat=3) if a+b+c == 2020][0]
    return first * second * third