def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip().split(" "))
            if line.startswith("addx"):
                full_list.append(["wait"])

    return full_list


def part1(parsed):
    x = 1
    termin = 0
    total = 0
    for cycle, command in enumerate(parsed):

        if cycle == 220:
            break
        if command[0] == "nood":
            continue
        if command[0] == "addx":
            termin = int(command[1])

        if cycle in (19, 59, 99, 139, 179, 219):
            total = total + (x * (cycle + 1))

        if command[0] == "wait":
            x += termin
            termin = 0
    return total


if __name__ == "__main__":
    parsed = parse("input/day10.txt")
    x = 1
    termin = 0
    pixel = (x-1, x, x+1)
    line = ["."]*40

    with open("res.txt", "w") as out:
        for cycle, command in enumerate(parsed):
            if (cycle+1)%40 == 0:
                out.write(''.join(line))
                out.write("\n")
                line = ["."]*40

            if command[0] == "addx":
                termin = int(command[1])

            if cycle%40 in pixel:
                line[cycle%40] = "#"

            if command[0] == "wait":
                x += termin
                pixel = (x - 1, x, x + 1)

    print(part1(parsed))
