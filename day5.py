import re
from collections import deque


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip())

    return full_list


def get_stacks(file):
    lines = []
    for line in file:
        if line.startswith("1"):
            break
        lines.append(line)
    stacks = [deque() for i in range(0, len(lines[-1]))]
    for i, stack in enumerate(stacks):
        for line in lines:
            if len(line) > i:
                if line[i].strip():
                    stack.append(line[i].strip())
    result = [s for s in stacks if ('[' not in s and "]" not in s and any(s))]
    return result


if __name__ == "__main__":
    parsed = parse('input/day5.txt')
    stacks = get_stacks(parsed)
    # print(stacks)
    for line in parsed:
        if not line.startswith("move"):
            continue
        el_num, stack_source, stack_target = re.findall(r'\d+', line)
        temp = []
        for i in range(0, int(el_num)):
            temp.append(stacks[int(stack_source)-1].popleft())
        for el in reversed(temp):
            stacks[int(stack_target)-1].appendleft(el)

    print(''.join([s.popleft() for s in stacks]))


