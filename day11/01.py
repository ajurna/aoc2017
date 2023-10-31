from typing import NamedTuple


class HexPoint(NamedTuple):
    q: int
    r: int
    s: int

    def __add__(self, other: "HexPoint"):
        return HexPoint(self.q + other.q, self.r + other.r, self.s + other.s)

    def distance(self, other: "HexPoint"):
        return (abs(self.q - other.q) + abs(self.r - other.r) + abs(self.s - other.s)) // 2

    def step(self, direction):
        directions = {
            'n': HexPoint(0, -1, 1),
            'ne': HexPoint(1, -1, 0),
            'se': HexPoint(1, 0, -1),
            's': HexPoint(0, 1, -1),
            'sw': HexPoint(-1, 1, 0),
            'nw': HexPoint(-1, 0, 1)
        }
        return self + directions[direction]


with open('01.txt') as f:
    data = f.read().split(',')

start = HexPoint(0,0,0)
p = start
furthest = 0
for d in data:
    p = p.step(d)
    furthest = max(p.distance(start), furthest)
print("Part 1:", p.distance(start))
print("Part 2:", furthest)
