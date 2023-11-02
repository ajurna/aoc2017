from collections import deque

spinlock = 303

data = deque([0])

for x in range(1, 2018):
    data.rotate(-(spinlock % len(data))-1)
    data.appendleft(x)


print("Part 1:", data[data.index(2017)+1])

data = deque([0])
idx = 0
for x in range(1, 50000000+1):
    data.rotate(-(spinlock % len(data))-1)
    data.appendleft(x)

print("Part 2:", data[data.index(0)+1])
