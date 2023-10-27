from typing import List

memory = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]


def rebalance(mem: List[int]):
    max_value = max(mem)
    max_index = mem.index(max_value)
    mem[max_index] = 0
    current_index = max_index
    while max_value:
        current_index = (current_index + 1) % len(mem)
        mem[current_index] += 1
        max_value -= 1
    return mem


def part1(mem: List[int]):
    visited = set()
    steps = 0
    while tuple(mem) not in visited:
        visited.add(tuple(mem))
        steps += 1
        mem = rebalance(mem)
    return steps, mem


def part2(mem: List[int]):
    steps = 1
    new_state = rebalance(mem.copy())
    while new_state != mem:
        new_state = rebalance(new_state)
        steps += 1
    return steps


p1, loop_memory = part1(memory)
print("Part 1:", p1)
print("Part 2:", part2(loop_memory))
