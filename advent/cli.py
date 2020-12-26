"""
The command line to run the actual code
"""
import click

from . import (
    day01,
    day02,
    day03,
    day04,
    day05,
    day06,
    day07,
    day08,
    day09,
    day10,
    day11,
    day12,
    day13,
    day14,
    day15,
    day16,
    day17,
    day18,
    day19,
    day20,
    day21,
    day22,
    day23,
    day24,
    day25,
)


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


@cli.command("day09")
@click.argument("filename")
def day09_command(filename: str):
    """ Day 9 """
    click.echo(f"The answer to part 1 is: {day09.first(filename)}")
    click.echo(f"The answer to part 2 is: {day09.second(filename)}")


@cli.command("day10")
@click.argument("filename")
def day10_command(filename: str):
    """ Day 10 """
    click.echo(f"The answer to part 1 is: {day10.first(filename)}")
    click.echo(f"The answer to part 2 is: {day10.second(filename)}")


@cli.command("day11")
@click.argument("filename")
def day11_command(filename: str):
    """ Day 11 """
    click.echo(f"The answer to part 1 is: {day11.first(filename)}")
    click.echo(f"The answer to part 2 is: {day11.second(filename)}")


@cli.command("day12")
@click.argument("filename")
def day12_command(filename: str):
    """ Day 12 """
    click.echo(f"The answer to part 1 is: {day12.first(filename)}")
    click.echo(f"The answer to part 2 is: {day12.second(filename)}")


@cli.command("day13")
@click.argument("filename")
def day13_command(filename: str):
    """ Day 13 """
    click.echo(f"The answer to part 1 is: {day13.first(filename)}")
    click.echo(f"The answer to part 2 is: {day13.second(filename)}")


@cli.command("day14")
@click.argument("filename")
def day14_command(filename: str):
    """ Day 14 """
    click.echo(f"The answer to part 1 is: {day14.first(filename)}")
    click.echo(f"The answer to part 2 is: {day14.second(filename)}")


@cli.command("day15")
@click.argument("filename")
def day15_command(filename: str):
    """ Day 15 """
    click.echo(f"The answer to part 1 is: {day15.first(filename)}")
    click.echo(f"The answer to part 2 is: {day15.second(filename)}")


@cli.command("day16")
@click.argument("filename")
def day16_command(filename: str):
    """ Day 16 """
    click.echo(f"The answer to part 1 is: {day16.first(filename)}")
    click.echo(f"The answer to part 2 is: {day16.second(filename)}")


@cli.command("day17")
@click.argument("filename")
def day17_command(filename: str):
    """ Day 17 """
    click.echo(f"The answer to part 1 is: {day17.first(filename)}")
    click.echo(f"The answer to part 2 is: {day17.second(filename)}")


@cli.command("day18")
@click.argument("filename")
def day18_command(filename: str):
    """ Day 18 """
    click.echo(f"The answer to part 1 is: {day18.first(filename)}")
    click.echo(f"The answer to part 2 is: {day18.second(filename)}")


@cli.command("day19")
@click.argument("filename")
def day19_command(filename: str):
    """ Day 19 """
    click.echo(f"The answer to part 1 is: {day19.first(filename)}")
    click.echo(f"The answer to part 2 is: {day19.second(filename)}")


@cli.command("day20")
@click.argument("filename")
def day20_command(filename: str):
    """ Day 20 """
    click.echo(f"The answer to part 1 is: {day20.first(filename)}")
    click.echo(f"The answer to part 2 is: {day20.second(filename)}")


@cli.command("day21")
@click.argument("filename")
def day21_command(filename: str):
    """ Day 21 """
    click.echo(f"The answer to part 1 is: {day21.first(filename)}")
    click.echo(f"The answer to part 2 is: {day21.second(filename)}")


@cli.command("day22")
@click.argument("filename")
def day22_command(filename: str):
    """ Day 22 """
    click.echo(f"The answer to part 1 is: {day22.first(filename)}")
    click.echo(f"The answer to part 2 is: {day22.second(filename)}")


@cli.command("day23")
@click.argument("filename")
def day23_command(filename: str):
    """ Day 23 """
    click.echo(f"The answer to part 1 is: {day23.first(filename)}")
    click.echo(f"The answer to part 2 is: {day23.second(filename)}")


@cli.command("day24")
@click.argument("filename")
def day24_command(filename: str):
    """ Day 24 """
    click.echo(f"The answer to part 1 is: {day24.first(filename)}")
    click.echo(f"The answer to part 2 is: {day24.second(filename)}")


@cli.command("day25")
@click.argument("filename")
def day25_command(filename: str):
    """ Day 25 """
    click.echo(f"The answer to part 1 is: {day25.first(filename)}")
    click.echo(f"The answer to part 2 is: {day25.second(filename)}")


if __name__ == "__main__":
    cli()
