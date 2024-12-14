cache = {}


def answer(stone, n_blinks):
    if n_blinks == 0:
        return 1  # just the length of that one number
    if (stone, n_blinks) not in cache:
        if stone == 0:
            result = answer(1, n_blinks - 1)
        elif len(str(stone)) % 2 == 0:  # Even number of digits
            stone = str(stone)
            result = 0
            result += answer(int(stone[: len(stone) // 2]), n_blinks - 1)
            result += answer(int(stone[len(stone) // 2 :]), n_blinks - 1)
            result = result
        else:
            result = answer(stone * 2024, n_blinks - 1)
        cache[(stone, n_blinks)] = result
    return cache[(stone, n_blinks)]


with open("day11/input.txt") as f:
    stones = list(map(int, f.read().strip().split(" ")))
    blinks = 75
    total_number_of_stones = 0
    for stone in stones:
        total_number_of_stones += answer(stone, blinks)
    print(total_number_of_stones)
