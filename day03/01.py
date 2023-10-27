from collections import defaultdict
from typing import NamedTuple


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
        return [self + p for p in
                [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0), Point(-1, -1), Point(1, -1), Point(-1, 1),
                 Point(1, 1)]]


def find_coord(target):
    layer = 0

    while target > (2 * layer + 1) ** 2:
        layer += 1
    square_max = (2 * layer + 1) ** 2

    side_length = (square_max - (2 * (layer - 1) + 1) ** 2) // 4

    if target in range(square_max - side_length + 1, square_max + 1):
        # bottom
        x = range(square_max - side_length + 1, square_max + 1).index(target) + 1 - side_length // 2
        y = layer
    elif target in range(square_max - side_length * 2 + 1, square_max - side_length + 1):
        # left
        x = -layer
        y = range(square_max - side_length * 2 + 1, square_max - side_length + 1).index(target) + 1 - side_length // 2
    elif target in range(square_max - side_length * 3 + 1, square_max - side_length * 2 + 1):
        # top
        y = -layer
        x = -(range(square_max - side_length * 3 + 1, square_max - side_length * 2 + 1).index(
            target) + 1 - side_length // 2)
    elif target in range(square_max - side_length * 4 + 1, square_max - side_length * 3 + 1):
        # right
        y = -(range(square_max - side_length * 4 + 1, square_max - side_length * 3 + 1).index(
            target) + 1 - side_length // 2)
        x = layer
    return Point(x, y)


def part2(t: int):
    spiral = defaultdict(int)
    spiral[Point(0,0)] = 1
    current_point = 2
    while True:
        coord = find_coord(current_point)
        val = sum(spiral[p] for p in coord.neighbours())
        spiral[coord] = val
        if val > t:
            break
        current_point += 1
    return val


p1 =  find_coord(265149)
print("Part 1:", p1.x+p1.y)
print("Part 2:", part2(265149))
