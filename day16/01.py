import re
from collections import deque
from functools import lru_cache
from typing import NamedTuple, Union


class Move(NamedTuple):
    action: str
    a: Union[int, str]
    b: Union[int, str] = ''


def dance(programs: str, i: int = 1) -> str:
    for j in range(i):
        programs = do_dance(programs)
    return programs


@lru_cache
def do_dance(programs):
    moves = move_list
    data = deque(programs)
    for move in moves:
        match move.action:
            case 's':
                data.rotate(move.a)
            case 'x':
                t = data[move.a]
                data[move.a] = data[move.b]
                data[move.b] = t
            case 'p':
                a = data.index(move.a)
                b = data.index(move.b)
                t = data[a]
                data[a] = data[b]
                data[b] = t
    return ''.join(data)


move_list = []
with open('01.txt') as f:
    for m in re.findall(r"(?P<op>\w)((?P<a>[a-z0-9]+)/(?P<b>[a-z0-9]+)|(?P<c>\d+))", f.read()):
        match m[0]:
            case 's':
                move_list.append(Move('s', int(m[1])))
            case 'x':
                move_list.append(Move('x', int(m[2]), int(m[3])))
            case 'p':
                move_list.append(Move('p', m[2], m[3]))

# 'abcdefghijklmnop'
# 'abcde'
dancers = 'abcdefghijklmnop'
print(dance(dancers))
print(dance(dancers, 1_000_000_000))
