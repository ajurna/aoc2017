from collections import deque
from functools import reduce
from itertools import batched
from typing import NamedTuple, List, Deque


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def neighbours(self):
        # up = Point(0, -1)
        # down = Point(0, 1)
        # left = Point(-1, 0)
        # right = Point(1, 0)
        # top_left = Point(-1, -1)
        # top_right = Point(1, -1)
        # bottom_left = Point(-1, 1)
        # bottom_right = Point(1, 1)
        return [self+p for p in [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)]]


def knot_hash(operations, width=256):
    if isinstance(operations, str):
        operations = [ord(c) for c in operations]
    operations.extend([17, 31, 73, 47, 23])
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
    return "".join(f"{d:02x}" for d in [reduce(lambda a, b: a ^ b, batch) for batch in batched(circle, 16)])


def scan_drive(start: Point, area: List[List[int]]):
    visited = set()
    visited.add(start)
    queue: Deque[Point] = deque()
    queue.append(start)
    while queue:
        p = queue.popleft()
        for n in p.neighbours():
            try:
                if area[n.y][n.x]:
                    if n in visited:
                        continue
                    visited.add(n)
                    queue.append(n)
            except IndexError:
                continue
    return visited


drive = []
unseen = []
for row in range(128):
    h = knot_hash([ord(c) for c in f"amgozmfv-{row}"])
    r = bin(int(h, 16))[2:].zfill(128)
    unseen += [Point(x, row) for x, p in enumerate(r) if p == '1']
    drive.append(r)

print("Part 1:", len(unseen))

count = 0
while unseen:
    queued = [unseen[0]]
    while queued:
        p = queued.pop()
        if p in unseen:
            unseen.remove(p)
            queued += p.neighbours()
    count += 1
print("Part 2:", count)
