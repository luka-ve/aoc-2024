import io
from math import ceil
from typing import Any

TEST_RESULT = ""


def part_1(file: io.TextIOWrapper) -> Any:
    rules, nums = file.read().split("\n\n")

    rules = [rule.split("|") for rule in rules.split("\n")]

    come_after: dict[str : set[str]] = {}

    for rule in rules:
        if come_after.get(rule[0]):
            come_after[rule[0]].add(rule[1])
        else:
            come_after[rule[0]] = {rule[1]}

    num_rows = [num_row.split(",") for num_row in nums.split("\n")]

    def is_sorted(row: list[str]) -> bool:
        for i in range(len(row) - 1):
            if not set(row[(i + 1) :]).issubset(come_after.get(row[i], {})):
                return False

        return True

    result = 0
    for row in num_rows:
        if is_sorted(row):
            result += int(row[len(row) // 2])

    return result


def part_2(file: io.TextIOWrapper) -> Any:
    rules, nums = file.read().split("\n\n")

    rules = [rule.split("|") for rule in rules.split("\n")]

    come_after: dict[str : set[str]] = {}

    for rule in rules:
        if come_after.get(rule[0]):
            come_after[rule[0]].add(rule[1])
        else:
            come_after[rule[0]] = {rule[1]}

    num_rows = [num_row.split(",") for num_row in nums.split("\n")]

    def is_sorted(row: list[str]) -> bool:
        for i in range(len(row) - 1):
            if not set(row[(i + 1) :]).issubset(come_after.get(row[i], {})):
                return False

        return True

    def correct_order(row: list[str]) -> list[str]:
        pass

    result = 0
    for row in num_rows:
        if is_sorted(row):
            result += int(row[len(row) // 2])

    return result
