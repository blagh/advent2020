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

REQUIRED_FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

class Passport:

    def __init__(self, passport):
        self.fields = { f.split(":")[0]: (f.split(":")[1]) for f in passport.split(" ") }
        self.valid_fields = { field: False for field in REQUIRED_FIELDS }
        self.is_valid = self._check_valid()

    def _check_valid(self):
        all_valid = True

        for field in REQUIRED_FIELDS:
            is_valid = self._check_valid_field(field, self.fields.get(field))
            self.valid_fields[field] = is_valid
            all_valid = all_valid and is_valid

        return all_valid

    def _check_valid_field(self, field_name, field_value):
        if (field_value == None):
            return False

        if field_name == "byr":
            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            return self._validate_year(field_value, 1920, 2002)

        if field_name == "iyr":
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            return self._validate_year(field_value, 2010, 2020)

        if field_name == "eyr":
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            return self._validate_year(field_value, 2020, 2030)

        if field_name == "hgt":
            # hgt (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            try:
                qty = int(field_value[:-2])
                unit = field_value[-2:]
                if unit == "cm":
                    return 150 <= qty and 193 >= qty
                if unit == "in":
                    return 59 <= qty and 76 >= qty
                return False
            except:
                return False

        if field_name == "hcl":
            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            if field_value[0] != "#":
                return False
            if len(field_value) != 7:
                return False
            return True

        if field_name == "ecl":
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            return field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if field_name == "pid":
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            if len(field_value) != 9:
                return False
            try:
                int(field_value)
                return True
            except:
                return False

        return False

    def _validate_year(self, value, min_year, max_year):
        if len(value) != 4:
            return False

        year = int(value)
        return min_year <= year and max_year >= year

    def print(self):
        pretty = " ".join(REQUIRED_FIELDS)
        for field in REQUIRED_FIELDS:
            is_good = self.valid_fields[field]
            pretty = set_color(pretty, pretty.index(field), is_good, 4)

        correct = "✅" if self.is_valid else "❌"

        print(correct + ": " + pretty + "\n" + str(self.fields))

# cid (Country ID) - ignored, missing or not.

passports = []

with open("day4input.txt") as file:
    lines = file.readlines()
    passport = ""
    for line in lines:
        if line == "\n":
            passports.append(Passport(passport[1:])) # strip initial empty char
            passport = ""
        else:
            passport += " " + line[:-1] # strip newline

# append the last passport
passports.append(Passport(passport[1:]))
correct = 0

for passport in passports:
    if passport.is_valid:
        correct += 1

    passport.print()


print(correct)
