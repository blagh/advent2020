outputs = []

with open("day08.txt") as file:
    outputs = [o[:-1] for o in file.readlines()]

# part 1
# count = 0
# for o in outputs:
#     digits = o.split(" | ")[1].split(" ")
#     filtered = list(filter(lambda d: len(d) in (2, 3, 4, 7), digits))
#     print(digits, filtered, len(filtered))
#     count += len(filtered)
#
# print(count)

# 000
# 1 2
# 333
# 4 5
# 666
ZER = {0, 1, 2, 4, 5, 6}
ONE = {2, 5}
TWO = {0, 2, 3, 4, 6}
THR = {0, 2, 3, 5, 6}
FOU = {1, 2, 3, 5}
FIV = {0, 1, 3, 5, 6}
SIX = {0, 1, 3, 4, 5, 6}
SEV = {0, 2, 5}
EIG = {0, 1, 2, 3, 4, 5, 6}
NIN = {0, 1, 2, 3, 5, 6}
DIGITS = [ZER, ONE, TWO, THR, FOU, FIV, SIX, SEV, EIG, NIN]

def safe_remove(value, list):
    if value in list:
        list.remove(value)

    return list

def filter_cands(d_set, actuals, cands):
    print("filter ~~~", d_set, actuals)

    if len(cands) == 1:
        return cands

    if len(d_set) == 6: # 6, 9, or 0
        if len(actuals[2]) == 1 and actuals[2] & d_set:
            print("   not 6")
            cands = safe_remove(6, cands)
        if len(actuals[4]) == 1 and actuals[4] & d_set:
            print("   not 9")
            cands = safe_remove(9, cands)
        if len(actuals[3]) == 1 and actuals[3] & d_set:
            print("   not 0")
            cands = safe_remove(0, cands)

        if len(actuals[2]) == 2 and (actuals[2] & d_set == actuals[2]):
            print("   not 6")
            cands = safe_remove(6, cands)
        if len(actuals[4]) == 2 and (actuals[4] & d_set == actuals[4]):
            print("   not 9")
            cands = safe_remove(9, cands)
        if len(actuals[3]) == 2 and (actuals[3] & d_set == actuals[3]):
            print("   not 0")
            cands = safe_remove(0, cands)

    elif len(d_set) == 5: # 2, 3, or 5
        if len(actuals[4]) == 1:
            if list(actuals[4])[0] in d_set:
                print("    it's 2")
                return [2]
            else:
                print("    not 2")
                cands = safe_remove(2, cands)

        if len(actuals[1]) == 1:
            if list(actuals[1])[0] in d_set:
                print("    it's 5")
                return [5]
            else:
                print("     not 5")
                cands = safe_remove(5, cands)

        if len(actuals[5]) == 1 and actuals[5] & d_set:
            print("    not 2")
            cands = safe_remove(2, cands)
        if len(actuals[2]) == 1 and actuals[2] & d_set:
            print("    not 5")
            cands = safe_remove(5, cands)

        if len(actuals[5]) == 2 and actuals[5] & d_set == actuals[5]:
            print("    not 2")
            cands = safe_remove(2, cands)
        if len(actuals[2]) == 2 and actuals[2] & d_set == actuals[2]:
            print("    not 5")
            cands = safe_remove(5, cands)

    print(cands)
    return cands

def reactualize(actuals, digit_set, positions):
    # intersect actuals with digit_set at positions
    # subtract digit_set from actuals at non-positions
    for i in range(7):
        if i in positions:
            actuals[i] = actuals[i] & digit_set
        else:
            actuals[i] = actuals[i] - digit_set

def simplify(actuals, candidates, input_digits):
    for a in actuals:
        if len(a) != 1:
            return False, candidates, actuals

    print("actuals are sorted out!")

    for i in range(len(actuals)):
        if type(actuals[i]) is set:
            (actuals[i],) == actuals[i]

    all_done = True
    for c in candidates:
        if type(c) is list:
            print("but we still got work to do")
            all_done = False
            break

    return all_done, candidates, actuals


def analyze(digit_text):
    text_len = len(digit_text)
    digit_sets = [set(d) for d in digit_text]
    actuals = [{"a", "b", "c", "d", "e", "f", "g"}] * 7

    digits = [None] * text_len

    print("---------")
    print(digit_text)

    for i in range(text_len):
        d_set = digit_sets[i]

        if len(d_set) == 2:
            digits[i] = 1
            reactualize(actuals, d_set, ONE)
        elif len(d_set) == 3:
            digits[i] = 7
            reactualize(actuals, d_set, SEV)
        elif len(d_set) == 4:
            digits[i] = 4
            reactualize(actuals, d_set, FOU)
        elif len(d_set) == 5:
            digits[i] = [2, 3, 5]
        elif len(d_set) == 6:
            digits[i] = [6, 9, 0]
        elif len(d_set) == 7:
            digits[i] = 8

    print(" ---")
    print(digits)
    print(actuals)

    sorted_out = False
    retry = True
    while not sorted_out and retry:
        retry = False

        for i in range(text_len):
            print("***new word***", digit_text[i])

            if type(digits[i]) is int:
                # we already matched this character to a digit
                print("it's", digits[i])
                continue

            d_set = digit_sets[i]
            digits[i] = filter_cands(d_set, actuals, digits[i])

            if len(digits[i]) == 1:
                # we figured one out!
                # filter out of other lists

                actual_digit = digits[i][0]
                print("we got it!", actual_digit)
                print("we should filter out", digit_sets[i])

                for j in range(len(digits)):
                    if digit_sets[i] == digit_sets[j]:
                        digits[j] = actual_digit
                    if type(digits[j]) is list:
                        safe_remove(actual_digit, digits[j])

                reactualize(actuals, d_set, DIGITS[actual_digit])

                print("so we've got", digits, actuals)
                (sorted_out, digits, actuals) = simplify(actuals, digits, digit_sets)

                print(digits)
                print(actuals)

                retry = True

    return digits, actuals

sum = 0
for o in outputs:
    print()
    print()
    print("***************************")

    all_digits = "".join(o.split(" |")).split(" ")

    digits, actuals = analyze(all_digits)

    print(digits)
    print(all_digits)
    print(actuals)

    print(o)
    our_digits = o.split(" | ")[1].split(" ")
    print(our_digits)
    we_want = digits[len(digits) - len(our_digits):]
    print(we_want)
    str_we_want = "".join([str(w) for w in we_want])
    print(str_we_want)

    sum += int(str_we_want)

print(sum)
