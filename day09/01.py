with open('01.txt') as f:
    data = f.read()


def scan(river):
    depth = 0
    score = 0
    garbage_removed = 0
    in_garbage = False
    ignore_next = False
    for c in river:
        if ignore_next:
            ignore_next = False
            continue
        if in_garbage:
            match c:
                case '!':
                    ignore_next = True
                case '>':
                    in_garbage = False
                case _:
                    garbage_removed += 1
        else:
            match c:
                case '{':
                    depth += 1
                    score += depth
                case '}':
                    depth -= 1
                case '<':
                    in_garbage = True
                case '!':
                    ignore_next = True
    return score, garbage_removed


results = scan(data)
print("Part 1:", results[0])
print("Part 2:", results[1])