import re

class Password:
    def __init__(self, line):
       lowerLimit, higherLimit, self.char, self.password = self.parseLine(line)
       self.lowerLimit = int(lowerLimit)
       self.higherLimit = int(higherLimit)

    def parseLine(self, line):
        p = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
        m = p.match(line)
        return m.groups()

    def isValid(self):
        return self.lowerLimit <= self.password.count(self.char) <= self.higherLimit

    def isReallyValid(self):
        c1, c2 = self.password[self.lowerLimit - 1], self.password[self.higherLimit - 1]
        return (c1 == self.char) ^ (c2 == self.char)

def solver(input, validCheck):
    passwords = [Password(line) for line in input.split('\n')]
    return len(p for p in passwords if validCheck(p))

def solve1(input):
    return solver(input, lambda p: p.is_valid())

def solve2(input):
    return solver(input, lambda p: p.isReallyValid())