import re
from collections import defaultdict


def parse(filepath):
    with open(filepath) as f:
        full_list = []
        for line in f:
            full_list.append(line.strip())

    return full_list


if __name__ == "__main__":
    parsed = parse('input/day7.txt')
    current_dir = ""
    result = defaultdict(lambda: [])
    for row in parsed:
        if "$ cd" in row:
            folder = row.split(" ")[-1]
            if folder == "..":
                current_dir = current_dir[0:-len(current_dir.split("/")[-2])]
            elif folder == "/":
                current_dir = folder
            else:
                current_dir = current_dir+folder+"/" if current_dir else folder
        if "$ ls" in row:
            continue
        result[current_dir] += [int(s) for s in re.findall(r"^\d+", row)]

    # print(json.dumps(result))
    sizes_dict = defaultdict(lambda: 0)
    for k, v in result.items():
        path = ""
        for part in k.rstrip("/").split("/"):
            path += part
            sizes_dict[path] += sum(v)

    free_space = 70000000 - sizes_dict[""]
    needed_space = 30000000 - free_space

    for v in sorted(sizes_dict.values()):
        if v > needed_space:
            print(v)
            break






