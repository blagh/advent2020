passwords = []

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

class Password:

    def __init__(self, min, max, char_, pass_):
        self.min_count = min
        self.max_count = max
        self.character = char_
        self.password = pass_
        self.is_valid = self._is_valid_two()
        self.correct = "✅" if self.is_valid else "❌"

    def _is_valid_two(self):
        position_one = self.min_count - 1
        position_two = self.max_count - 1

        if position_one > len(self.password):
            return false

        if position_two > len(self.password):
            return self.password[position_one] == self.character

        return (self.password[position_one] == self.character) ^ (self.password[position_two] == self.character)

    def _is_valid_one(self):
        required_character_count = len(list(filter(lambda x: x == self.character, self.password)))
        # print(self.password, self.min_count, required_character_count, self.max_count)
        return self.min_count <= required_character_count and self.max_count >= required_character_count

    def _pretty_password(self):
        pretty = self.password
        p_one = self.min_count - 1
        p_two = self.max_count - 1

        pretty = self._set_color(pretty, p_two, self.password[p_two] == self.character)
        pretty = self._set_color(pretty, p_one, self.password[p_one] == self.character)

        print(pretty, self.password)

        return pretty

    def _set_color(self, pretty, p, is_good):
        color = bcolors.OKGREEN if is_good else bcolors.FAIL
        return pretty[:p] + color + pretty[p] + bcolors.ENDC + pretty[p+1:]

    def __repr__(self):
        return f'{self.correct}: {self.min_count}-{self.max_count} {self.character}: {self._pretty_password()}'

with open("day2input.txt") as file:
    for line in file.readlines():
        # 4-5 l: rllllj
        tokens = line.split(" ")
        min_max = tokens[0].split("-")
        character = tokens[1][0]
        password = tokens[2]

        passwords += [Password(int(min_max[0]), int(min_max[1]), character, password)]

print(passwords)

valid_passwords = list(filter(lambda p: p.is_valid, passwords))
print(valid_passwords)
print(len(valid_passwords))
