from collections import Counter

with open("input.txt") as f:
    left, right = zip(*[map(int, line.strip().split("   ")) for line in f])
    left = sorted(left)
    right = sorted(right)
    occurences = Counter(right)
    print(sum([left[i] * occurences[left[i]] for i in range(len(left))]))