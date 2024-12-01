from pathlib import Path
import click
import importlib
from time import time


@click.command()
@click.argument("day")
def aoc(day: str):
    module = importlib.import_module(f"{day}.solution")

    for part in (module.part_1, module.part_2):
        for inp in ("test_input.txt", "input.txt"):
            with open(Path.cwd() / day / inp) as f:
                t0 = time()
                result = part(f)
                print(
                    f"{part.__name__} ran in {((time() - t0) * 1000):.5f} ms on {inp}"
                )
                print(result)


if __name__ == "__main__":
    aoc()
