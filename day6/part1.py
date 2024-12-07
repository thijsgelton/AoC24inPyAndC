import numpy as np


directions = ["^", "<", ">", "v"]


def go_left(patrol_map, position, facing):
    patrol_map[*position] = "X"
    position = position - (0, 1)
    patrol_map[*position] = facing
    return position


def go_up(patrol_map, position, facing):
    patrol_map[*position] = "X"
    position = position - (1, 0)
    patrol_map[*position] = facing
    return position


def go_right(patrol_map, position, facing):
    patrol_map[*position] = "X"
    position = position + (0, 1)
    patrol_map[*position] = facing
    return position


def go_down(patrol_map, position, facing):
    patrol_map[*position] = "X"
    position = position + (1, 0)
    patrol_map[*position] = facing
    return position


with open(r"C:\Users\thijs\Programming\AoC24inPyAndC\day6\input.txt") as f:
    patrol_map = np.array([list(l.strip()) for l in f.readlines()])
    position = None
    facing = None
    for i, row in enumerate(patrol_map):
        for j, cell in enumerate(row):
            if cell in directions:
                position = np.array([i, j])
                facing = cell

    in_map = True
    while in_map:
        try:
            if facing == "v":
                if patrol_map[*(position + (1, 0))] != "#":
                    position = go_down(patrol_map, position, facing)
                else:
                    facing = "<"
                    position = go_left(patrol_map, position, facing)
            elif facing == "^":
                if patrol_map[*(position - (1, 0))] != "#" and position[0] > 0:
                    position = go_up(patrol_map, position, facing)
                elif position[0] == 0:
                    in_map = False
                    break
                else:
                    facing = ">"
                    position = go_right(patrol_map, position, facing)
            elif facing == "<":
                if patrol_map[*(position - (0, 1))] != "#" and position[1] > 0:
                    position = go_left(patrol_map, position, facing)
                elif position[1] == 0:
                    in_map = False
                    break
                else:
                    facing = "^"
                    position = go_up(patrol_map, position, facing)
            elif facing == ">":
                if patrol_map[*(position + (0, 1))] != "#":
                    position = go_right(patrol_map, position, facing)
                else:
                    facing = "v"
                    position = go_down(patrol_map, position, facing)
        except IndexError:
            in_map = False
            open("output.txt", "w").write(
                "\n".join(["".join(row) for row in patrol_map])
            )
    print(sum([cell == "X" for row in patrol_map for cell in row]) + 1)
