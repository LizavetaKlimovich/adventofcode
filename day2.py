score = {"A": 1,  # rock
         "B": 2,  # paper
         "C": 3,  # scissors
         "X": 1,
         "Y": 2,
         "Z": 3}


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.split())

    return full_list


def beats(value):
    if value == 3:
        return 1
    elif value == 2:
        return 3
    elif value == 1:
        return 2


def looses(value):
    if value == 3:
        return 2
    elif value == 2:
        return 1
    elif value == 1:
        return 3


if __name__ == "__main__":
    parsed = parse('./day2.txt')
    total = 0
    for you, me in parsed:
        if me == "X":
            my_point = looses(score[you])
        elif me == "Y":
            my_point = score[you]
            total += 3
        else:
            my_point = beats(score[you])
            total += 6
        total += my_point
    print(total)
