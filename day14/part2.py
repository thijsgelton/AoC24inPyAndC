from collections import deque

from tqdm import tqdm


def get_regions(cmap):
    regions = []
    seen = set()

    for r in range(wide):
        for c in range(tall):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            region = {(r, c)}
            q = deque([(r, c)])
            letter = cmap[r][c]
            if letter == ".":
                continue

            while q:
                cr, cc = q.popleft()
                for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if nr < 0 or nr >= wide or nc < 0 or nc >= tall:
                        continue
                    if cmap[nr][nc] != letter:
                        continue
                    if (nr, nc) in region:
                        continue
                    region.add((nr, nc))
                    q.append((nr, nc))
            seen |= region
            regions.append(region)
    return regions


with open("day14/input.txt") as f:
    robots = []
    tall = 103
    wide = 101
    seconds = 100
    quads = [0, 0, 0, 0]
    robots = list(f.readlines())

    for seconds in tqdm(range(0, 10000)):
        christmas_map = [["." for _ in range(tall)] for _ in range(wide)]
        for l in robots:
            l = l.strip()
            pos, vel = l.split(" ")
            pos_x, pos_y = list(map(int, pos.strip("p=").split(",")))
            vel_x, vel_y = list(map(int, vel.strip("v=").split(",")))
            next_x = (pos_x + seconds * vel_x) % wide
            next_y = (pos_y + seconds * vel_y) % tall
            christmas_map[next_x][next_y] = "#"
            # if next_x < (wide // 2) and next_y < (tall // 2):
            #     quads[0] += 1
            # elif next_x < (wide // 2) and next_y > (tall // 2):
            #     quads[1] += 1
            # elif next_x > (wide // 2) and next_y < (tall // 2):
            #     quads[2] += 1
            # elif next_x > (wide // 2) and next_y > (tall // 2):
            #     quads[3] += 1
        # print(christmas_map)
        regions = get_regions(christmas_map)
        for region in regions:
            if len(region) > 100:
                print(seconds)
                break
        # print([len(region) for region in regions])

    # print(quads[0] * quads[1] * quads[2] * quads[3])
