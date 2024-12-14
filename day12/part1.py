from collections import deque


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def compute_perimeter(r, c, garden):
    perimeter = 0
    for dr, dc in directions:
        if 0 <= r + dr < len(garden) and 0 <= c + dc < len(garden[0]):
            if garden[r + dr][c + dc] != garden[r][c]:
                perimeter += 1
        else:  # out of bounds
            perimeter += 1
    return perimeter


with open("day12/input.txt") as f:
    garden = [list(l.strip()) for l in f.readlines()]
    rows, cols = len(garden[0]), len(garden)

    regions = []
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            region = {(r, c)}
            q = deque([(r, c)])
            crop = garden[r][c]

            while q:
                cr, cc = q.popleft()
                for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if garden[nr][nc] != crop:
                        continue
                    if (nr, nc) in region:
                        continue
                    region.add((nr, nc))
                    q.append((nr, nc))
            seen |= region
            regions.append(region)

    total = 0

    for region in regions:
        perimeter = 0
        for r, c in region:
            perimeter += compute_perimeter(r, c, garden)
        total += len(region) * perimeter

    print(total)
