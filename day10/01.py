from collections import deque
from itertools import batched
from functools import reduce

def tie_part1(width: int, operations):
    circle = deque(range(width))
    temp = deque()
    offset = 0
    skip_size = 0

    for op in operations:
        for _ in range(op):
            temp.append(circle.popleft())
        for _ in range(op):
            circle.appendleft(temp.popleft())
        offset = (offset + op + skip_size) % len(circle)
        circle.rotate(-(op + skip_size) % len(circle))
        skip_size += 1

    circle.rotate(offset)
    return circle[0] * circle[1]


def tie_part2(width: int, operations):
    circle = deque(range(width))
    temp = deque()
    offset = 0
    skip_size = 0
    for _ in range(64):
        for op in operations:
            for _ in range(op):
                temp.append(circle.popleft())
            for _ in range(op):
                circle.appendleft(temp.popleft())
            offset = (offset + op + skip_size) % len(circle)
            circle.rotate(-(op + skip_size) % len(circle))
            skip_size += 1

    circle.rotate(offset)
    return circle


print("Part 1:", tie_part1(256, [46, 41, 212, 83, 1, 255, 157, 65, 139, 52, 39, 254, 2, 86, 0, 204]))

p2_ops = [ord(c) for c in "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204"]
p2_ops.extend([17, 31, 73, 47, 23])

dense = [reduce(lambda a, b: a ^ b, batch) for batch in batched(tie_part2(256, p2_ops), 16)]

print("Part 2:", "".join(f"{d:02x}" for d in dense))

