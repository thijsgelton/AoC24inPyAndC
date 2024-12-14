from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def walk_route(r, c, topographic_map):
    q = deque([(r, c)])
    seen = set()
    peaks = 0

        r, c = q.popleft()
        value = topographic_map[r][c]
        for dr, dc in directions:
            if (r + dr, c + dc) in seen:
                continue
            if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                continue
            seen.add((r + dr, c + dc))
            if topographic_map[r + dr][c + dc] == 9:
                peaks += 1
                continue
            if topographic_map[r + dr][c + dc] == value + 1:
                q.append((r + dr, c + dc))
    return peaks


with open("day10/test_input.txt") as f:
    total = 0
    topographic_map = [list(map(int, l.strip())) for l in f.readlines()]
    rows, cols = len(topographic_map), len(topographic_map[0])
    for r in range(rows):
        for c in range(cols):
            if topographic_map[r][c] == 0:
                total += walk_route(r, c, topographic_map)
    print(total)
