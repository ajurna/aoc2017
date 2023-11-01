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
        return [np for p in
                [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)] if (np := (self+p)).x > 0 and np.y > 0]

def hash(operations, width=256):
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

drive = []
unseen = []
for row in range(128):
    h = hash([ord(c) for c in f"flqrgnkx-{row}"])
    r = list(int(x) for x in ''.join([f"{int(c, 16):04b}" for c in h]))
    unseen += [Point(x, row) for x, p in enumerate(r) if p == 1]
    drive.append(r)

print(len(unseen))


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


count = 0
visited = set()
for y, row in enumerate(drive):
    for x, sector in enumerate(row):
        location = Point(x, y)
        if location not in visited:
            if drive[y][x] == 1:
                count += 1
                visited |= scan_drive(location, drive)
print(count)
print(len(visited))
