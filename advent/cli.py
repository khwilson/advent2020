"""
The command line to run the actual code
"""
import click

from . import day01, day02, day03


@click.group()
def cli():
    """ Advent of Code 2020 """


@cli.command("day01")
@click.argument("filename")
def day01_command(filename: str):
    """ Day 1 """
    click.echo(f"The answer to part 1 is: {day01.first(filename)}")
    click.echo(f"The answer to part 2 is: {day01.second(filename)}")


@cli.command("day02")
@click.argument("filename")
def day02_command(filename: str):
    """ Day 2 """
    click.echo(f"The answer to part 1 is: {day02.first(filename)}")
    click.echo(f"The answer to part 2 is: {day02.second(filename)}")


@cli.command("day03")
@click.argument("filename")
def day03_command(filename: str):
    """ Day 3 """
    click.echo(f"The answer to part 1 is: {day03.first(filename)}")
    click.echo(f"The answer to part 2 is: {day03.second(filename)}")


if __name__ == "__main__":
    cli()
