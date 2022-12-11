from collections import defaultdict, Counter


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append([int(i) for i in line.strip()])

    return full_list


def part1(parsed):
    counter = 0
    for i, line in enumerate(parsed):
        for j, tree in enumerate(line):
            if (i == 0 or i + 1 == len(parsed)) or (j == 0 or j + 1 == len(line)):
                counter += 1
                continue
            if all([tree > el for el in line[0:j]]) or all([tree > el for el in line[j + 1:]]):
                counter += 1
                continue
            if all([tree > l[j] for l in parsed[0:i]]) or all([tree > l[j] for l in parsed[i + 1:]]):
                counter += 1
                continue
    return counter


def find_scenery(tree, line, do_reverse):
    local_counter = 0
    for x, el in enumerate(reversed(line) if do_reverse else line):
        # print(tree, el, line[0:j])
        if tree > el:
            local_counter += 1
            if x + 1 == len(line):
                local_counter = local_counter if local_counter else 1
                # print(local_counter)
                return local_counter
        else:
            local_counter = local_counter + 1 if local_counter else 1
            # print(local_counter)
            return local_counter


if __name__ == "__main__":
    parsed = parse('input/day8.txt')

    counter = defaultdict(lambda: 1)
    for i, line in enumerate(parsed):
        for j, tree in enumerate(line):
            if (i == 0 or i + 1 == len(parsed)) or (j == 0 or j + 1 == len(line)):
                continue
            # if i == 3 and j == 2:
            code = str(i) + "." + str(j)
            counter[code] = counter[code] * find_scenery(tree, line[0:j], True)
            counter[code] = counter[code] * find_scenery(tree, line[j + 1:], False)
            counter[code] = counter[code] * find_scenery(tree, [l[j] for l in parsed[0:i]], True)
            counter[code] = counter[code] * find_scenery(tree, [l[j] for l in parsed[i + 1:]], False)
        # break

    print(Counter(counter).most_common(1))
