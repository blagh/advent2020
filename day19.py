from itertools import product
from collections import defaultdict


RULES = {}
TAB = "  "
STASH = defaultdict(dict)

class OptionRule:
    def __init__(self, options):
        self.options = [FollowRule(o) for o in options]

    def _get_stash(self, key):
        return STASH[repr(self)].get(key)

    def _set_stash(self, key, value):
        STASH[repr(self)][key] = value

    # def generate_messages(self, rules, depth):
    #     print(TAB*depth, "OPTION", self.options)
    #     messages = sum([o.generate_messages(rules, depth+1) for o in self.options], [])
    #     print(TAB*depth, "OPTION", messages)
    #     return messages

    def matches(self, message, depth):
        options = list(filter(lambda o: len(o) <= len(message), self.options))
        if len(options) == 0:
            print(TAB*depth, "OPTION FAIL - NO OPTIONS", message)
            return False, message

        if result := self._get_stash(message):
            print(TAB*depth, "OPTION STASH", message, result)
            return result

        print(TAB*depth, "OPTION", message, options)

        matches = []
        for o in options:
            # print(TAB*depth, o)
            (did_match, sub_matches) = o.matches(message, depth+1)
            if did_match:
                if type(sub_matches) == list:
                    matches += sub_matches
                else:
                    matches.append(sub_matches)

        if len(matches) == 1:
            print(TAB*depth, "OPTION SUCCESS", matches[0])
            return self._return(message, True, matches[0])

        if len(matches) > 0:
            print(TAB*depth, "OPTION MULTI SUCCESS", matches)
            return self._return(message, True, matches)

        print(TAB*depth, "OPTION FAIL", message)
        return self._return(message, False, message)

    def _return(self, original_message, success, message):
        self._set_stash(original_message, (success, message))
        return success, message

    def __repr__(self):
        return " | ".join([repr(o) for o in self.options])

class FollowRule:
    def __init__(self, follows):
        self.follows = [ReferenceRule(f) for f in follows]

    def _get_stash(self, key):
        return STASH[repr(self)].get(key)

    def _set_stash(self, key, value):
        STASH[repr(self)][key] = value

    # def generate_messages(self, rules, depth):
    #     messages = [""]
    #     print(TAB*depth, "FOLLOW", self.follows)
    #
    #     for f in self.follows:
    #         print(TAB*depth, f)
    #         sub = f.generate_messages(rules, depth+1)
    #         messages = ["".join(a) for a in list(product(messages, sub))]
    #
    #     print(TAB*depth, "FOLLOW", messages)
    #     return messages

    def matches(self, message, depth):
        original_message = message
        if self._get_stash(message):
            print(TAB*depth, "FOLLOW STASH", self._get_stash(message))
            return self._get_stash(message)

        if len(message) < len(self.follows):
            print(TAB*depth, "FOLLOW FAILURE -- TOO SHORT!", original_message)
            return False, original_message

        print(TAB*depth, "FOLLOW", message, self.follows)
        for f in self.follows:
            # print(TAB*depth, f)

            (did_match, message) = f.matches(message, depth+1)
            if not did_match:
                print(TAB*depth, "FOLLOW FAILURE", original_message)
                return self._return(False, original_message, original_message)

        print(TAB*depth, "FOLLOW SUCCESS", message)
        return self._return(True, original_message, message)

    def _return(self, success, original, message):
        self._set_stash(original, (success, message))
        return success, message

    def __len__(self):
        return len(self.follows)

    def __repr__(self):
        return " ".join([repr(f) for f in self.follows])

class ReferenceRule:
    def __init__(self, rule_no):
        self.rule_no = rule_no

    def _get_stash(self, key):
        return STASH[repr(self)].get(key)

    def _set_stash(self, key, value):
        STASH[repr(self)][key] = value

    def matches(self, message, depth):
        if result := self._get_stash(message):
            print(TAB*depth, "REF STASH", message, result)
            return result

        print(TAB*depth, "REF", message, self.rule_no)
        matches = RULES[self.rule_no].matches(message, depth+1)
        print(TAB*depth, "REF", matches)
        return self._return(message, *matches)

    def _return(self, original_message, success, message):
        self._set_stash(original_message, (success, message))
        return (success, message)

    def __repr__(self):
        return repr(self.rule_no)

class Rule:
    def __init__(self, value):
        self.value = value

    def matches(self, message, depth):
        print(TAB*depth, "RULE", message, self.value)

        if len(message) == 0:
            print(TAB*depth, "RULE FAIL :/ NO MOAR MESSAGE")
            return False, ""

        if type(message) == list:
            sub_matches = []
            for m in message:
                if m and m[0] == self.value:
                    sub_matches.append(m[1:])

            if len(sub_matches) == 1:
                return True, sub_matches[0]

            if len(sub_matches) > 0:
                return True, sub_matches

            return False, message

        if message[0] == self.value:
            print(TAB*depth, "RULE SUCCESS!", message[0], message[1:])
            return True, message[1:]

        print(TAB*depth, "RULE FAIL :/", message)
        return False, message

    def __repr__(self):
        return repr(self.value)

with open("day19rules.txt") as file:
    for line in file.readlines():
        tokens = line[:-1].split(": ")
        rule_no = int(tokens[0])
        rule = tokens[1]

        if "|" in rule:
            rule = OptionRule([[int(n) for n in o.split(" ")] for o in rule.split(" | ")])
        elif " " in rule:
            rule = FollowRule([int(n) for n in rule.split(" ")])
        else:
            if rule[1].isnumeric():
                rule = ReferenceRule(int(rule))
            else:
                rule = Rule(rule[1])

        RULES[rule_no] = rule

for r in sorted(RULES.keys()):
    print(r, RULES[r])

# valid_messages = rules[0].generate_messages(rules, 0)
# print(valid_messages)

messages = []
with open("day19input.txt") as file:
    messages = [m[:-1] for m in file.readlines()]

actuals = []
for message in messages:
    print("---", message, "---")
    (did_match, match) = RULES[0].matches(message, 0)

    if did_match:
        print("--- MATCH!", message, "---")
        actuals.append(message)
    else:
        print("--- FAIL :/", message, "---")

print(actuals)
print(len(actuals))
