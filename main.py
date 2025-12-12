import time
from datetime import date
from rich.console import Console
from rich.table import Table

from day01.solution import Main as Day01
from day02.solution import Main as Day02
from day03.solution import Main as Day03
from day04.solution import Main as Day04
from day05.solution import Main as Day05
from day06.solution import Main as Day06
from day07.solution import Main as Day07
from day08.solution import Main as Day08
from day09.solution import Main as Day09
from day10.solution import Main as Day10
from day11.solution import Main as Day11
from day12.solution import Main as Day12

console = Console()
YEAR = 2025
DAY_CLASSES = [Day01, Day02, Day03, Day04, Day05, Day06, Day07, Day08, Day09, Day10, Day11, Day12]

def main():
    console.print("--------------------------------------------------------------------------------")
    print_trees(6, tree_count=5)
    print_all_results()

def print_trees(h, tree_count=2, gap=6):
    max_width = 2 * h - 1
    lines = []

    for i in range(h):
        stars = "*" * (2 * i + 1)
        line = (" " * gap).join(stars.center(max_width) for _ in range(tree_count))
        lines.append(line)
    trunk = (" " * gap).join("|".center(max_width) for _ in range(tree_count))
    lines.append(trunk)

    console.print("\n".join(lines), style="cyan")

def get_day_results(day_index, day_obj):
    if day_index == 2:
        return day_obj.part_one_greedy(), day_obj.part_two_greedy()
    elif day_index == 7:
        return day_obj.part_one(k=1000), day_obj.part_two()
    elif day_index == 11:
        return day_obj.part_one(), "—"
    else:
        return day_obj.part_one(), day_obj.part_two()

def print_all_results():
    today = date.today()
    open_day = today.day if today.year == YEAR else 0

    table = Table(title=f"Advent of Code {YEAR}")
    table.add_column("Day", justify="center")
    table.add_column("Link", overflow="fold")
    table.add_column("Part 1", justify="center")
    table.add_column("Part 2", justify="center")

    start = time.time()

    for i, DayClass in enumerate(DAY_CLASSES):
        day_num = i + 1
        link = f"https://adventofcode.com/{YEAR}/day/{day_num}" if day_num <= open_day else "—"

        if day_num <= open_day:
            day_obj = DayClass()
            try:
                p1, p2 = get_day_results(i, day_obj)
            except Exception as e:
                p1, p2 = "ERROR", str(e)
        else:
            p1, p2 = "—", "—"

        table.add_row(str(day_num), link, str(p1), str(p2))

    end = time.time()

    console.print(table)
    console.print(f"AoC-2025 total runtime: {end - start:.2f} seconds", style="bold green")

if __name__ == "__main__":
    main()
