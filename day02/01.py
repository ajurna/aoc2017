from itertools import combinations

data = []
with open('01.txt') as f:
    for line in f.readlines():
        line = list(map(int, line.strip().split()))
        data.append(line)

total = 0
for row in data:
    total += max(row) - min(row)
print("Part 1:", total)

total = 0
for row in data:
    for pair in combinations(row, 2):
        if max(pair) % min(pair) == 0:
            total += max(pair) // min(pair)
print("Part 1:", total)
