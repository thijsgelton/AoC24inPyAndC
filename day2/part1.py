from functools import reduce


with open("input.txt") as f:
    reports = [l.strip() for l in f.readlines()]
    count = 0
    for report in reports:
        levels = list(map(int, report.split(" ")))
        differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
        if all([-3 <= diff <= -1 for diff in differences]) or all(
            [1 <= diff <= 3 for diff in differences]
        ):
            count += 1
        else:
            continue
    print(count)
