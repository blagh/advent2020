required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def set_color(pretty, p, is_good, until=1):
    color = bcolors.OKGREEN if is_good else bcolors.FAIL
    return pretty[:p] + color + pretty[p:p+until] + bcolors.ENDC + pretty[p+until:]

passports = []

with open("day4input.txt") as file:
    lines = file.readlines()
    passport = ""
    for line in lines:
        if line == "\n":
            passports.append(passport[1:]) # strip initial empty char
            passport = ""
        else:
            passport += " " + line[:-1] # strip newline

# append the last passport
passports.append(passport[1:])
correct = 0

def print_passport(fields, correct, passport):
    pretty = " ".join(required_fields)
    for field in fields:
        is_good = True
        if field not in pretty:
            is_good = False
            pretty += " " + field

        pretty = set_color(pretty, pretty.index(field), is_good, 4)

    correct = "✅" if correct else "❌"

    print(correct + ": " + pretty + "\n" + passport)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# def is_valid(field)


for passport in passports:
    fields = passport.split(" ")
    field_names = set([f.split(":")[0] if (f and f.split(":")[1]) else "" for f in fields])

    is_correct = required_fields == (field_names & required_fields)
    if is_correct:
        correct += 1

    print_passport(field_names, is_correct, passport)


print(correct)
