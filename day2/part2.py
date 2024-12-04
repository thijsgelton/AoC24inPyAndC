from functools import reduce


def is_safe(levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    return increasing or decreasing


with open("input.txt") as f:
    reports = [l.strip() for l in f.readlines()]
    count = 0
    for report in reports:
        levels = list(map(int, report.split(" ")))
        if is_safe(levels) or any(
            [is_safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels))]
        ):
            count += 1

    print(count)
