import day4


def test_passport_constructor():
    assert day4.Passport("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm""").fields == {'byr': '1937', 'cid': '147', 'ecl': 'gry', 'eyr': '2020',
                                                   'hcl': '#fffffd', 'hgt': '183cm', 'iyr': '2017', 'pid': '860033327'}


def test_passport_valid():
    assert day4.Passport("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm""").is_valid() is True


def test_passport_valid_no_cid():
    assert day4.Passport("""hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm""").is_valid() is True


def test_passport_not_valid():
    assert day4.Passport("""iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929""").is_valid() is False


def test_passport_is_really_valid():
    assert day4.Passport("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f""").is_really_valid() is True
    assert day4.Passport("""eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm""").is_really_valid() is True
    assert day4.Passport("""hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022""").is_really_valid() is True
    assert day4.Passport("""iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""").is_really_valid() is True


def test_passport_is_really_valid_false():
    assert day4.Passport("""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926""").is_really_valid() is False
    assert day4.Passport("""iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946""").is_really_valid() is False
    assert day4.Passport("""
hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277""").is_really_valid() is False
    assert day4.Passport("""hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""").is_really_valid() is False


def test_solve1():
    with open('input.txt') as f:
        assert day4.solve1(f.read()) == 190


def test_solve2():
    with open('input.txt') as f:
        assert day4.solve2(f.read()) == 121
