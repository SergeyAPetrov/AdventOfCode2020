import math

def get_collision(line, index):
    return 1 if line[index % len(line)] == '#' else 0

def count_collisions(lines, *, di, dl):
    result, i = 0, 0
    while i*di<len(lines):
        result, i = result + get_collision(lines[i*di], i*dl), i + 1
    return result

def count_multiple_collisions(lines):
    indexes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    return math.prod([count_collisions(lines, di=di, dl=dl) for di, dl in indexes])