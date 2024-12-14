from collections import deque


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
corner_directions = [
    ((-1, 0), (0, 1)),
    ((0, -1), (1, 0)),
    ((1, 0), (0, 1)),
    ((-1, 0), (0, -1)),
]


def sides(region):
    edges = {}
    for r, c in region:
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in region:
                continue
            er = (r + nr) / 2
            ec = (c + nc) / 2
            edges[(er, ec)] = (er - r, ec - c)
    seen = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in seen:
            continue
        seen.add(edge)
        side_count += 1
        er, ec = edge
        if er % 1 == 0:
            for dr in [-1, 1]:
                cr = er + dr
                while edges.get((cr, ec)) == direction:
                    seen.add((cr, ec))
                    cr += dr
        else:
            for dc in [-1, 1]:
                cc = ec + dc
                while edges.get((er, cc)) == direction:
                    seen.add((er, cc))
                    cc += dc

    return side_count


with open("day12/input.txt") as f:
    garden = [list(l.strip()) for l in f.readlines()]
    rows, cols = len(garden), len(garden[0])

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

    print(sum(len(region) * sides(region) for region in regions))
