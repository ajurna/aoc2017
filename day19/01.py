from typing import NamedTuple
from itertools import takewhile

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

    def char(self, area):
        if 0 <= self.y < len(area) and 0 <= self.x <= len(area[self.y]):
            return area[self.y][self.x]
        return ' '

    def up(self):
        return self + Point(0, -1)

    def down(self):
        return self + Point(0, 1)

    def left(self):
        return self + Point(-1, 0)

    def right(self):
        return self + Point(1, 0)


area = []
with open('01.txt') as f:
    for line in f.readlines():
        area.append(list(line.strip('\n')))

start = Point(area[0].index('|'), 0)
last = start

word = []
steps = 1
while True:
    if start.up().char(area) != ' ' and start.up() != last:
        # print('up')
        line = list(takewhile(lambda y: y != ' ', (x[start.x] for x in area[start.y::-1] if x[start.x] != '')))
        word.extend(l for l in line if l.isalpha())
        start = Point(start.x, start.y - len(line) + 1)
        last = start.down()
    elif start.down().char(area) != ' ' and start.down() != last:
        # print('down')
        line = list(takewhile(lambda y: y != ' ', (x[start.x] for x in area[start.y:] if x[start.x] != '')))
        word.extend(l for l in line if l.isalpha())
        start = Point(start.x, start.y+len(line)-1)
        last = start.up()
    elif start.right().char(area) != ' ' and start.right() != last:
        # print('right')
        line = list(takewhile(lambda y: y != ' ', (x for x in area[start.y][start.x:] if x != '')))
        word.extend(l for l in line if l.isalpha())
        start = Point(start.x + len(line) - 1, start.y)
        last = start.left()
    elif start.left().char(area) != ' ' and start.left() != last:
        # print('left')
        line = list(takewhile(lambda y: y != ' ', (x for x in area[start.y][start.x::-1] if x != '')))
        word.extend(l for l in line if l.isalpha())
        start = Point(start.x - len(line) + 1, start.y)
        last = start.left()
    steps += len(line)-1
    if start.char(area) != '+':
        break


print("Part 1:", ''.join(word))
print("Part 2:", steps)
