import datetime
from pathlib import Path
import click
import importlib
import shutil
from time import time


@click.group(invoke_without_command=True)
@click.pass_context
def aoc(ctx):
    pass


@aoc.command()
@click.argument("day", default=datetime.datetime.today().day, type=str)
def run(day: str):
    module = importlib.import_module(f"{day}.solution")

    for part in (module.part_1, module.part_2):
        for inp in ("test_input.txt", "input.txt"):
            with open(Path.cwd() / day / inp) as f:
                t0 = time()
                result = part(f)
                click.echo(
                    f"{part.__name__} ran in {((time() - t0) * 1000):.5f} ms on {inp}"
                )
                click.echo(result)


@aoc.command()
@click.argument("day", default=datetime.datetime.today().day, type=str)
def create(day: str):
    path = Path.cwd() / day
    if path.exists():
        click.echo(f'Directory "{path.as_posix()}" already exists')
        return

    shutil.copytree("template", day)


if __name__ == "__main__":
    aoc()
