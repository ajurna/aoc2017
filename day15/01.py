
def generator1(gen, mul):
    while True:
        gen = (gen * mul) % 2147483647
        yield gen


def generator2(gen, mul, div):
    while True:
        gen = (gen * mul) % 2147483647
        if gen % div == 0:
            yield gen


def part1(gen_a=65, gen_b=8921):
    gen_a = generator1(gen_a, 16807)
    gen_b = generator1(gen_b, 48271)
    count = 0
    for _ in range(40_000_000):
        a = next(gen_a)
        b = next(gen_b)
        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1
    return count


def part2(gen_a=65, gen_b=8921):
    gen_a = generator2(gen_a, 16807, 4)
    gen_b = generator2(gen_b, 48271, 8)
    count = 0
    for _ in range(5_000_000):
        a = next(gen_a)
        b = next(gen_b)
        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1
    return count


print("Part 1:", part1(618, 814))
print("Part 2:", part2(618, 814))
