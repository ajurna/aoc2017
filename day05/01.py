with open('01.txt') as f:
    program = list(map(int, f.readlines()))


def part1(prog):
    index = 0
    steps = 0
    while index < len(prog):
        new_index = index + prog[index]
        prog[index] += 1
        index = new_index
        steps += 1
    return steps


def part2(prog):
    index = 0
    steps = 0
    while index < len(prog):
        new_index = index + prog[index]
        if prog[index] >= 3:
            prog[index] -= 1
        else:
            prog[index] += 1
        index = new_index
        steps += 1
    return steps


print("Part 1:", part1(program.copy()))
print("Part 2:", part2(program.copy()))
