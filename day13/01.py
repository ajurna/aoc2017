from typing import NamedTuple


class Scanner(NamedTuple):
    depth: int
    size: int

    def scanned(self, tick):
        return (self.size + tick) % self.size == 0

    def pendulum_position(self, tick):
        pos = tick % (2 * self.size - 2)
        if pos >= self.size:
            pos = self.size - (pos % self.size) - 2
        return pos

    def score(self):
        return self.depth * self.size


firewall = {}
with open('01.txt') as f:
    for line in f.readlines():
        depth, size = line.strip().split(': ')
        firewall[int(depth)] = Scanner(int(depth), int(size))


def calc_score(scanners, tick=0):
    score = 0
    for n in range(max(scanners.keys())+1):
        if n in scanners:
            if scanners[n].pendulum_position(n+tick) == 0:
                score += scanners[n].score()
    return score


def calc_pass(scanners, tick=0):
    for n in range(max(scanners.keys())+1):
        if n in scanners:
            if scanners[n].pendulum_position(n+tick) == 0:
                return False
    return True


def part2(scanners):
    current_tick = 0
    while not calc_pass(scanners, current_tick):
        current_tick += 1
    return current_tick


print("Part 1:", calc_score(firewall))
print("Part 2:", part2(firewall))
