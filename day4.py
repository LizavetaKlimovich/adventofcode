letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip().split(","))

    return full_list


if __name__ == "__main__":
    parsed = parse('input/day4.txt')
    count = 0
    group = []
    for line in parsed:
        set1 = set(range(int(line[0].split("-")[0]), int(line[0].split("-")[1])+1))
        set2 = set(range(int(line[1].split("-")[0]), int(line[1].split("-")[1])+1))
        if set1.intersection(set2):
            count +=1

    print(count)
