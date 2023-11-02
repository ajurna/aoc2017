import re
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Particle:
    id: int
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int
    ax: int
    ay: int
    az: int

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def distance_from_zero(self):
        return sum(map(abs, [self.x, self.y, self.z]))

    def __eq__(self, other: "Particle"):
        return self.x == other.x and self.y == other.y and self.z == other.z


particles = []
with open("01.txt") as f:
    for i, line in enumerate(f.readlines()):
        m = re.match(r"p=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>, v=<(?P<vx>-?\d+),(?P<vy>-?\d+),(?P<vz>-?\d+)>, "
                     r"a=<(?P<ax>-?\d+),(?P<ay>-?\d+),(?P<az>-?\d+)>", line)
        particles.append(Particle(i, *map(int, m.groups())))

for _ in range(1000):
    [p.tick() for p in particles]
l = sorted((p.distance_from_zero(), p.id) for p in particles)
print("Part 1:", l[0][1])

particles = []
with open("01.txt") as f:
    for i, line in enumerate(f.readlines()):
        m = re.match(r"p=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>, v=<(?P<vx>-?\d+),(?P<vy>-?\d+),(?P<vz>-?\d+)>, "
                     r"a=<(?P<ax>-?\d+),(?P<ay>-?\d+),(?P<az>-?\d+)>", line)
        particles.append(Particle(i, *map(int, m.groups())))

for _ in range(1000):
    [p.tick() for p in particles]
    to_remove = set()
    for p1, p2 in combinations(particles, 2):
        if p1 == p2:
            to_remove.add(p1.id)
            to_remove.add(p2.id)
    particles = [p for p in particles if p.id not in to_remove]
print("Part 2:", len(particles))
