with open("input.txt") as f:
    left, right = zip(*[map(int, line.strip().split("   ")) for line in f])
    left = sorted(left)
    right = sorted(right)
    print(sum([abs(left[i] - right[i]) for i in range(len(left))]))