from collections import Counter
total = 0
total2 = 0
with open('01.txt') as f:
    for line in f.readlines():
        l = line.strip().split()
        if len(l) == len(set(l)):
            total += 1
        if len(l) == len(set(tuple(sorted((k, v) for k, v in Counter(i).items())) for i in l)):
            total2 += 1
print("Part 1:", total)
print("Part 2:", total2)
