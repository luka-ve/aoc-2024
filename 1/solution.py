import bisect
import io
from typing import Any

TEST_RESULT = "11"


def part_1(file: io.TextIOWrapper) -> Any:
    left = []
    right = []

    for line in file:
        a, b = line.split()

        bisect.insort(left, int(a))
        bisect.insort(right, int(b))

    return sum([abs(pair[0] - pair[1]) for pair in zip(left, right)])


def part_2(file: io.TextIOWrapper) -> Any:
    left = {}
    right = {}

    for line in file:
        a, b = [int(x) for x in line.split()]

        left[a] = 1 if not left.get(a) else left[a] + 1
        right[b] = 1 if not right.get(b) else right[b] + 1

    similarity_score = 0

    for key in left.keys():
        similarity_score += key * (right.get(key, 0)) * left[key]

    return similarity_score
