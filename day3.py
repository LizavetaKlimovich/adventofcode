letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip())

    return full_list


def find_odd(line):
    set1 = set(line[0: len(line) // 2])
    set2 = set(line[len(line) // 2:])
    return set1.intersection(set2).pop()


def find_common_of_group(group):
    return group[0].intersection(group[1]).intersection(group[2]).pop()


if __name__ == "__main__":
    parsed = parse('./day3.txt')
    total = 0
    group = []
    for i, line in enumerate(parsed):
        if i>0 and (i) % 3 == 0:
            l = find_common_of_group(group)
            total += letters.index(l)
            group = []
            print(l, letters.index(l), total)
        group.append(set(line))
    l = find_common_of_group(group)
    total += letters.index(l)

    print(total)
