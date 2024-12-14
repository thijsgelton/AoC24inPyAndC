from collections import deque
from tqdm import tqdm


with open("day11/input.txt") as f:
    stones = deque(map(int, f.read().strip().split(" ")))
    blinks = 25
    operations = dict()
    for _ in tqdm(range(blinks)):
        next_stones = deque()
        while stones:
            stone = stones.popleft()
            if stone == 0:
                next_stones.append(1)
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                digits = list(map(int, str(stone)))
                mid = len(digits) // 2
                left = int("".join(map(str, digits[:mid])))
                right = int("".join(map(str, digits[mid:])))
                next_stones.append(left)
                next_stones.append(right)
            else:
                next_stones.append(stone * 2024)
        stones = next_stones
    print(len(stones))
