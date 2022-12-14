import copy

WIDTH = 1000
HIGH = 160
GRID = [["."] * WIDTH for _ in range(HIGH)]


def draw_stones(stones):
    for line in stones:
        dots = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in line.split(" -> ")]
        for i, dot in enumerate(dots):
            if i + 1 == len(dots):
                continue
            next_dot = dots[i + 1]
            for i in range(min(dot[0], next_dot[0]), max(dot[0], next_dot[0]) + 1):
                for j in range(min(dot[1], next_dot[1]), max(dot[1], next_dot[1]) + 1):
                    GRID[j][i] = "#"


def calculate(grid):
    sand = 0
    try:
        while True:
            x, y = (0, 500)
            while True:
                if grid[x + 1][y] == ".":
                    x += 1
                elif grid[x + 1][y - 1] == ".":
                    x, y = x + 1, y - 1
                elif grid[x + 1][y + 1] == ".":
                    x, y = x + 1, y + 1
                else:
                    grid[x][y] = "*"
                    sand += 1
                    if x == 0 and y == 500:
                        raise IndexError
                    break
    except IndexError:
        print("Number of sands: ", sand)


if __name__ == "__main__":
    stones = open("./input/day14.txt").read().strip().split("\n")

    draw_stones(stones)
    grid_p1 = copy.deepcopy(GRID)
    calculate(grid_p1)

    max_y = max([i for i, _ in enumerate(GRID) if "#" in _])

    GRID[max_y + 2] = ["#"] * WIDTH
    calculate(GRID)
