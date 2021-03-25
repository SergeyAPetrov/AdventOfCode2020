import re


class Passport:
    valid_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def __init__(self, line):
        parts = [tuple(char.split(":")) for char in re.split(r"\n|\s", line) if char != '']
        self.fields = {k: v for (k, v) in parts}

    def is_valid(self):
        return Passport.valid_fields <= set(self.fields.keys())

    def is_really_valid(self):
        return self.is_valid() \
               and self.validate_year("byr", 1920, 2002) \
               and self.validate_year("iyr", 2010, 2020) \
               and self.validate_year("eyr", 2020, 2030) \
               and self.validate_height() \
               and self.validate_hair_color() \
               and self.validate_eye_color() \
               and self.validate_passport_number()

    def validate_year(self, field, lower_limit, upper_limit):
        return lower_limit <= int(self.fields[field]) <= upper_limit

    def validate_height(self):
        match = re.match(r"(\d+)(in|cm)", self.fields["hgt"])
        if match is None:
            return False
        value, unit = match.groups()
        if unit == "cm":
            return 150 <= int(value) <= 193
        else:
            return 59 <= int(value) <= 76

    def validate_hair_color(self):
        return re.match(r"[#][0-9a-f]{6}", self.fields["hcl"]) is not None

    def validate_eye_color(self):
        return self.fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def validate_passport_number(self):
        try:
            int(self.fields["pid"])
        except ValueError:
            return False
        else:
            return len(self.fields["pid"]) == 9

    def validate_passport_number1(self):
        return re.match(r"^\d{9}$", self.fields["pid"]) is not None


def solve1(input):
    return solver(input, lambda p: p.is_valid())


def solve2(input):
    return solver(input, lambda p: p.is_really_valid())


def solver(input, is_valid_check):
    lines = input.split("\n\n")
    passports = [Passport(line) for line in lines]
    return len([p for p in passports if is_valid_check(p)])
