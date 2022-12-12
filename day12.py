from collections import deque


def bfs(grid, start, end):
    queue = deque([[start]])
    explored = {start}
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < 83 and 0 <= y2 < 41 and grid[y2][x2] - grid[y][x] <= 1 and (x2, y2) not in explored:
                queue.append(path + [(x2, y2)])
                explored.add((x2, y2))


if __name__ == "__main__":
    file = open("./input/day12.txt").read().strip().split()

    start = [(j, i) for i, l in enumerate(file) for j, s in enumerate(l) if s == "S"][0]
    print("start: ", start)
    end = [(j, i) for i, l in enumerate(file) for j, s in enumerate(l) if s == "E"][0]
    print("end: ", end)

    grid = [[ord(s.replace("S", "a").replace("E", "z")) for s in l] for l in file]
    # -1 because we don't count start
    print("part 1: ", len(bfs(grid, start, end)) - 1)

    # part 2
    starts = [(j, i) for i, l in enumerate(grid) for j, s in enumerate(l) if s == 97]
    roads = [len(bfs(grid, start, end)) - 1 for start in starts if bfs(grid, start, end)]
    print("part 2: ", sorted(roads)[0])
