import re


with open("day13/input.txt") as f:
    total_min_tokens = 0
    for prize_setup in f.read().split("\n\n"):
        buttons = prize_setup.split("\n")
        button_a = list(map(int, re.findall(r"(\d+)", buttons[0])))
        button_b = list(map(int, re.findall(r"(\d+)", buttons[1])))
        prize_location = list(map(int, re.findall(r"(\d+)", buttons[2])))
        pos = (0, 0)
        best = 99999
        for i in range(101):
            for j in range(101):
                pos = (
                    button_a[0] * i + button_b[0] * j,
                    button_a[1] * i + button_b[1] * j,
                )
                if pos[0] == prize_location[0] and pos[1] == prize_location[1]:
                    best = min(best, i * 3 + j)
        if best < 99999:
            total_min_tokens += best
    print(total_min_tokens)
