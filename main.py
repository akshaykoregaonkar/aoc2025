from day01.solution import Main as Day01
from day02.solution import Main as Day02
from day03.solution import Main as Day03
import time


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
    print("Day 3: greedy")
    start = time.time()
    print("part 1:", day03.part_one_greedy())
    print("part 2:", day03.part_two_greedy())
    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds")
    print("Day 3: slicing")
    start = time.time()
    print("part 1:", day03.part_one_slicing())
    print("part 2:", day03.part_two_slicing())
    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds")
    print("------------")


if __name__ == "__main__":
    main()
