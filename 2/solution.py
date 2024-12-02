import io
from typing import Any

TEST_RESULT = ""


def part_1(file: io.TextIOWrapper) -> Any:
    n_valid_reports = 0

    for line in file:
        report = [int(number) for number in line.split()]

        if check_report_validity(report):
            n_valid_reports += 1

    return n_valid_reports


def part_2(file: io.TextIOWrapper) -> Any:
    n_valid_reports = 0

    for line in file:
        report = [int(number) for number in line.split()]

        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)

            if check_report_validity(new_report):
                n_valid_reports += 1
                break

    return n_valid_reports


def check_report_validity(report: list[int]) -> bool:
    is_sorted = all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(
        report[i] >= report[i + 1] for i in range(len(report) - 1)
    )

    if not is_sorted:
        return False

    for i in range(0, len(report) - 1):
        diff = report[i] - report[i + 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True
