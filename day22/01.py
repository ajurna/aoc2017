from dataclasses import dataclass
from typing import NamedTuple, Dict


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
        return [self + p for p in [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)]]

    def up(self):
        return self + Point(0, -1)

    def down(self):
        return self + Point(0, 1)

    def left(self):
        return self + Point(-1, 0)

    def right(self):
        return self + Point(1, 0)


@dataclass
class Virus:
    location: Point
    direction: str = 'U'
    directions: str = 'URDL'
    infected_count: int = 0

    def __post_init__(self):
        pass

    def tick(self, area: Dict[Point, bool]):
        if area.get(self.location, False):
            del area[self.location]
            self.turn_right()
        else:
            area[self.location] = True
            self.infected_count += 1
            self.turn_left()
        self.move()

    def move(self):
        match self.direction:
            case 'U':
                self.location = self.location.up()
            case 'D':
                self.location = self.location.down()
            case 'L':
                self.location = self.location.left()
            case 'R':
                self.location = self.location.right()

    def turn_right(self):
        self.direction = self.directions[(self.directions.index(self.direction) + 1) % 4]

    def turn_left(self):
        self.direction = self.directions[self.directions.index(self.direction) - 1]


@dataclass
class Virus2(Virus):
    def tick(self, area: Dict[Point, str]):
        match area.get(self.location, 'clean'):
            case 'clean':
                self.turn_left()
                area[self.location] = 'weakened'
            case 'weakened':
                self.infected_count += 1
                area[self.location] = 'infected'
            case 'infected':
                self.turn_right()
                area[self.location] = 'flagged'
            case 'flagged':
                self.turn_left()
                self.turn_left()
                del area[self.location]
        self.move()


area = {}
area2 = {}

with open('01.txt') as f:
    for y, row in enumerate(f.readlines()):
        for x, char in enumerate(row.strip()):
            if char == '#':
                area[Point(x, y)] = True
                area2[Point(x, y)] = 'infected'
    virus = Virus(Point(x // 2, y // 2))
    virus2 = Virus2(Point(x // 2, y // 2))

for _ in range(10000):
    virus.tick(area)
print("Part 1:", virus.infected_count)

for _ in range(10000000):
    virus2.tick(area2)
print("Part 2:", virus2.infected_count)
