with open("day14/input.txt") as f:
    robots = []
    tall = 103
    wide = 101
    seconds = 100
    quads = [0, 0, 0, 0]
    for l in f.readlines():
        l = l.strip()
        pos, vel = l.split(" ")
        pos_x, pos_y = list(map(int, pos.strip("p=").split(",")))
        vel_x, vel_y = list(map(int, vel.strip("v=").split(",")))
        next_x = (pos_x + seconds * vel_x) % wide
        next_y = (pos_y + seconds * vel_y) % tall
        if next_x < (wide // 2) and next_y < (tall // 2):
            quads[0] += 1
        elif next_x < (wide // 2) and next_y > (tall // 2):
            quads[1] += 1
        elif next_x > (wide // 2) and next_y < (tall // 2):
            quads[2] += 1
        elif next_x > (wide // 2) and next_y > (tall // 2):
            quads[3] += 1
    print(quads[0] * quads[1] * quads[2] * quads[3])
