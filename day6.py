import re
from collections import deque


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip())

    return full_list


if __name__ == "__main__":
    parsed = parse('./day6.txt')
    for line in parsed:
        for i, letter in enumerate(line):
            if len(set(line[i: i+14])) == 14:
                print(i+14)
                break





