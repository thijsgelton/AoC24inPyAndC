from enum import Enum
from pprint import pprint


class Facing(Enum):
    UP = "^"
    LEFT = "<"
    RIGHT = ">"
    DOWN = "v"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return k
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


with open(
    r"C:\Users\tgelton\Projects\Persoonlijk\AoC24inPyAndC\day6\test_input.txt"
) as f:
    patrol_map = [list(l.strip()) for l in f.readlines()]
    starting_position = None
    facing = None
    for i, row in enumerate(patrol_map):
        for j, cell in enumerate(row):
            if cell in Facing.list():
                starting_position = (i, j)
                facing = Facing.value_of(cell)
    in_map = True
    while in_map:
        pprint(patrol_map)
        try:
            if facing is Facing.DOWN:
                if patrol_map[starting_position - (1, 0)] != "#":
                    patrol_map[starting_position + (1, 0)] = "X"
                    starting_position = starting_position + (1, 0)
                else:
                    facing = Facing.LEFT
            elif facing is Facing.UP:
                if patrol_map[starting_position + (1, 0)] != "#":
                    patrol_map[starting_position + (1, 0)] + "X"
                    starting_position = starting_position + (1, 0)
                else:
                    facing = Facing.RIGHT
            elif facing is Facing.LEFT:
                if patrol_map[starting_position - (0, 1)] != "#":
                    patrol_map[starting_position - (0, 1)] = "X"
                    starting_position = starting_position - (0, 1)
                else:
                    facing = Facing.UP
            elif facing is Facing.RIGHT:
                if patrol_map[starting_position + (0, 1)] != "#":
                    patrol_map[starting_position + (0, 1)] = "X"
                    starting_position = starting_position + (0, 1)
                else:
                    facing = Facing.DOWN
        except IndexError:
            in_map = False
    print(sum([cell for row in patrol_map for cell in row if cell == "X"]))
