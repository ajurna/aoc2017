from collections import deque
from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Connector:
    a: int
    b: int

    def __post_init__(self):
        self.a = int(self.a)
        self.b = int(self.b)

    @property
    def ports(self):
        return [self.a, self.b]

    def connect(self, port):
        if self.a == port:
            return self.b
        return self.a

    def __hash__(self):
        return hash(f'{self.a}/{self.b}')

    @property
    def val(self):
        return self.a + self.b


connectors = set()
with open('01.txt') as f:
    for line in f.readlines():
        connector = Connector(*line.strip().split('/'))
        connectors.add(connector)


def find_longest(connectors):
    queue = deque()
    largest = 0
    longest_length = 0
    longest_strength = 0
    for connector in connectors:
        if 0 in connector.ports:
            open = connector.connect(0)
            queue.append(({connector}, open))
    while queue:
        used, next_port = queue.popleft()
        for connector in connectors - used:
            if next_port in connector.ports:
                open = connector.connect(next_port)
                new_used = used | {connector}
                queue.append((new_used, open))
                score = sum(c.val for c in new_used)
                if largest <= score:
                    largest = score
                if len(new_used) == longest_length:
                    if score > longest_strength:
                        longest_strength = score
                elif len(new_used) > longest_length:
                    longest_length = len(new_used)
                    longest_strength = score
    return largest, longest_strength


part_1, part_2 = find_longest(connectors)
print("Part 1:", part_1)
print("Part 2:", part_2)