from typing import List

import numpy as np
from numpy.typing import ArrayLike


def parse_src(s: str) -> List[ArrayLike]:
    groups = []
    for g in s.split('/'):
        groups.append([0 if i == '.' else 1 for i in g])
    array = np.array(groups)
    out = []
    for a in [array, np.fliplr(array)]:
        out.extend([
            a,
            np.rot90(a, 1),
            np.rot90(a, 2),
            np.rot90(a, 3)
        ])
    return out


def parse_dst(s: str) -> ArrayLike:
    groups = []
    for g in s.split('/'):
        groups.append([0 if i == '.' else 1 for i in g])
    return np.array(groups)


def flatten(iterable):
    result = []
    for elem in iterable:
        if isinstance(elem, (list, tuple)):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return tuple(result)


rules = {}
with open('01.txt') as f:
    for line in f.readlines():
        src, dst = line.strip().split(' => ')
        dst = parse_dst(dst)
        for s in parse_src(src):
            rules[tuple(tuple(tuple(i) for i in s))] = dst

area = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
for it in range(18):
    new_rows = []
    if area.shape[0] % 2 == 0:
        new_rows = []
        for row in np.vsplit(area, area.shape[0]//2):
            new_cols = []
            for col in np.hsplit(row, area.shape[0]//2):
                new_cols.append(rules[tuple(tuple(tuple(i) for i in col))])
            new_rows.append(np.concatenate(new_cols, 1))
        area = np.concatenate(new_rows)
    else:
        new_rows = []
        for row in np.vsplit(area, area.shape[0]//3):
            new_cols = []
            for col in np.hsplit(row, area.shape[0]//3):
                new_cols.append(rules[tuple(tuple(tuple(i) for i in col))])
            new_rows.append(np.concatenate(new_cols, 1))
        area = np.concatenate(new_rows)
    if it == 4:
        print("Part 1:", np.sum(area))
print("Part 2:", np.sum(area))
