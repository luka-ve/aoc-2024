import io
from typing import Any
import re
from math import prod

TEST_RESULT = ""


def part_1(file: io.TextIOWrapper) -> Any:
    return sum([int(pair[0]) * int(pair[1]) for pair in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file.read())])

def part_2(file: io.TextIOWrapper) -> Any:
    return sum([int(pair[0]) * int(pair[1]) for pair in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", re.sub(r"don't.*?(do(?!n't)|$)", "", file.read().replace("\n", ""), count=0))])
