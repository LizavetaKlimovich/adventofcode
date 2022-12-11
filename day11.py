import copy
import math
from collections import namedtuple, Counter
import re
from functools import reduce

Monkey = namedtuple("Monkey", "items,operation,test,if_true,if_false")


def parse(filepath):
    monkeys = []

    f = iter(open(filepath).read().strip("\n").split("\n"))

    while True:
        try:
            x = next(f)
        except StopIteration:
            break

        if x.startswith("Monkey"):
            items = [int(i) for i in re.findall(r"\d+", next(f))]
            op = next(f).split("old ")[-1].split(" ")
            test = [int(i) for i in re.findall(r"\d+", next(f))][0]
            if_true = [int(i) for i in re.findall(r"\d+", next(f))][0]
            if_false = [int(i) for i in re.findall(r"\d+", next(f))][0]
            monkey = Monkey(items, op, test, if_true, if_false)
            monkeys.append(monkey)
    return monkeys


if __name__ == "__main__":
    monkeys = parse("input/day11.txt")
    common_div = reduce(lambda x, y: x*y, [m.test for m in monkeys])
    counter = Counter()
    for i in range(10000):
        for monkey in monkeys:
            for j, item in enumerate(copy.deepcopy(monkey.items)):
                op = item if monkey.operation[1] == "old" else int(monkey.operation[1])
                worry_level = item+op if monkey.operation[0] == "+" else item*op
                # part 1:
                # new_wl = math.floor(worry_level/3)
                new_wl = worry_level
                if new_wl % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(new_wl%common_div)
                else:
                    monkeys[monkey.if_false].items.append(new_wl%common_div)
                del monkey.items[0]
                counter[monkey.test] += 1

    print(counter.most_common(2)[0][1] * counter.most_common(2)[1][1])
