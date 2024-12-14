import re

import numpy as np


with open("day13/input.txt") as f:
    total_min_tokens = 0
    for prize_setup in f.read().split("\n\n"):
        buttons = prize_setup.split("\n")
        button_a = np.array(list(map(int, re.findall(r"(\d+)", buttons[0]))))
        button_b = np.array(list(map(int, re.findall(r"(\d+)", buttons[1]))))
        p = list(map(int, re.findall(r"(\d+)", buttons[2])))
        p[0] += 10000000000000
        p[1] += 10000000000000
        R = np.linalg.solve(np.array([button_a, button_b]).T, [[p[0]], [p[1]]])
        print(R)
        atimes = round(R[0, 0])
        btimes = round(R[1, 0])
        if atimes * button_a[0] + btimes * button_b[0] == p[0] and (
            atimes * button_a[1] + btimes * button_b[1] == p[1]
        ):
            total_min_tokens += int(atimes * 3 + btimes)

    print(total_min_tokens)
