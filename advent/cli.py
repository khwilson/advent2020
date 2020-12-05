"""
The command line to run the actual code
"""
import click

from . import day01, day02, day03, day04, day05, day06, day07, day08


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


@cli.command("day04")
@click.argument("filename")
def day04_command(filename: str):
    """ Day 4 """
    click.echo(f"The answer to part 1 is: {day04.first(filename)}")
    click.echo(f"The answer to part 2 is: {day04.second(filename)}")


@cli.command("day05")
@click.argument("filename")
def day05_command(filename: str):
    """ Day 5 """
    click.echo(f"The answer to part 1 is: {day05.first(filename)}")
    click.echo(f"The answer to part 2 is: {day05.second(filename)}")


@cli.command("day06")
@click.argument("filename")
def day06_command(filename: str):
    """ Day 6 """
    click.echo(f"The answer to part 1 is: {day06.first(filename)}")
    click.echo(f"The answer to part 2 is: {day06.second(filename)}")


@cli.command("day07")
@click.argument("filename")
def day07_command(filename: str):
    """ Day 7 """
    click.echo(f"The answer to part 1 is: {day07.first(filename)}")
    click.echo(f"The answer to part 2 is: {day07.second(filename)}")


@cli.command("day08")
@click.argument("filename")
def day08_command(filename: str):
    """ Day 8 """
    click.echo(f"The answer to part 1 is: {day08.first(filename)}")
    click.echo(f"The answer to part 2 is: {day08.second(filename)}")


if __name__ == "__main__":
    cli()
