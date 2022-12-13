from itertools import zip_longest
import re
import json


def compare(left, right):
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    for el1, el2 in zip_longest(left, right):
        if isinstance(el1, int) and isinstance(el2, int):
            if el1 > el2:
                return False
            elif el1 == el2:
                continue
            else:
                return True
        elif el1 is None:
            return True
        elif el2 is None:
            return False
        else:
            x = compare(el1, el2)
            if x is not None:
                return x


def sort_key(l):
    # god forgive me for that
    l = l.replace("[]", "[0]")
    return [int(_) for _ in re.findall(r"\d+", l)]


if __name__ == "__main__":

    input = open("./input/day13.txt").read().split("\n\n")

    total = 0
    for i, pair in enumerate(input):
        left, right = pair.split("\n")
        left = json.loads(left)
        right = json.loads(right)
        res = compare(left, right)
        if res:
            total += (i + 1)
    print("Part 1: ", total)

    dividers = ["[[2]]", "[[6]]"]
    input2 = [l for l in open("./input/day13.txt").read().strip().split("\n") if l]

    input2.extend(dividers)

    print("Part 2: ", (sorted(input2, key=sort_key).index(dividers[0])+1) * (sorted(input2, key=sort_key).index(dividers[1])+1))
