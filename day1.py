def parse(filepath):
    with open(filepath) as f:
        full_list = []
        elf = []
        for line in f:
            if line.strip() == '':
                full_list.append(elf)
                elf = []
            else:
                elf.append(int(line.strip()))

    return full_list

sum3 = 0
for i, el in enumerate(sorted([sum(i) for i in parse('./elfs.txt')], reverse=True)):
    if i < 3:
        sum3 += el

print(sum3)