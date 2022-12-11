import numpy as np


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip().split(" "))

    return full_list


def move_tail(head, tail):
    dist = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    if head[0] == tail[0] and dist >= 2:
        return [tail[0], head[1] - np.sign(head[1] - tail[1])]
    if head[1] == tail[1] and dist >= 2:
        return [head[0] - np.sign(head[0] - tail[0]), tail[1]]
    if dist > 2:
        if head[0] > tail[0]:
            return [tail[0] + 1, tail[1] + np.sign(head[1] - tail[1])]
        if head[0] < tail[0]:
            return [tail[0] - 1, tail[1] + np.sign(head[1] - tail[1])]
    return tail


if __name__ == "__main__":
    parsed = parse('input/day9.txt')
    directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

    head = [0, 0]
    tails = [[0, 0] for i in range(9)]
    total = ["0.0"]

    for direction, num in parsed:
        num = int(num)
        for i in range(num):
            head = [sum(el) for el in zip(head, directions.get(direction))]
            prev_tail = head
            for v, tail in enumerate(tails):
                tails[v] = move_tail(prev_tail, tail)
                if v == 8:
                    total.append(str(tail[0]) + "." + str(tail[1]))
                prev_tail = tails[v]

    print(len(set(total)))
