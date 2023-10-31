from collections import defaultdict, deque
from typing import Set, Dict

area = defaultdict(set)
with open('01.txt') as f:
    for line in f.readlines():
        p, conns = line.strip().split(' <-> ')
        conns = conns.split(', ')
        for c in conns:
            area[int(p)].add(int(c))

def search_part1(start: int, graph: Dict[int, Set]):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    count = 0
    while queue:
        position = queue.popleft()
        count += 1
        for n in graph[position]:
            if n in visited:
                continue
            visited.add(n)
            queue.append(n)
    return visited


print("Part 1:", len(search_part1(0, area)))
all_nodes = set(area.keys())
visited = set()
count = 0
while len(all_nodes) != len(visited):
    next_node = list(all_nodes - visited)[0]
    visited |= search_part1(next_node, area)
    count += 1
print("Part 2:", count)
