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

def main():
    day01 = Day01()
    print("Day 1")
    print("part 1:", day01.part_one())
    print("part 2:", day01.part_two())
    print("------------")

    day02 = Day02()
    print("Day 2")
    print("part 1:", day02.part_one())
    print("part 2:", day02.part_two())
    print("------------")

    day03 = Day03()
    print("Day 3")
    print("part 1:", day03.part_one_greedy())
    print("part 2:", day03.part_two_greedy())
    print("------------")

    day04 = Day04()
    print("Day 4")
    print("part 1:", day04.part_one())
    print("part 2:", day04.part_two())
    print("------------")

    day05 = Day05()
    print("Day 5")
    print("part 1:", day05.part_one())
    print("part 2:", day05.part_two())
    print("------------")

    day06 = Day06()
    print("Day 6")
    print("part 1:", day06.part_one())
    print("part 2:", day06.part_two())
    print("------------")

    day07 = Day07()
    print("Day 7")
    print("part 1:", day07.part_one())
    print("part 2:", day07.part_two())
    print("------------")

    day08 = Day08()
    print("Day 8")
    print("part 1:", day08.part_one(k=1000))
    print("part 2:", day08.part_two())
    print("------------")

    day09 = Day09()
    print("Day 9")
    print("part 1:", day09.part_one())
    print("part 2:", day09.part_two())
    print("------------")

    day10 = Day10()
    print("Day 10")
    print("part 1:", day10.part_one())
    print("part 2:", day10.part_two())

if __name__ == "__main__":
    main()
