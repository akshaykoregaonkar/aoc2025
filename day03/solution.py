def _load_banks():
    with open("input/day3.txt") as f:
        return [[int(d) for d in line.strip()] for line in f]


def _largest_jolts(bank, k=2):
    stack = []
    n = len(bank)
    to_remove = n - k

    # greedy stack - remove any smaller batteries
    for battery in bank:
        while stack and stack[-1] < battery and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append(battery)

    return int("".join(map(str, stack[:k])))


class Main:
    def __init__(self):
        self.banks = _load_banks()

    def part_one(self):
        return sum(_largest_jolts(i) for i in self.banks)

    def part_two(self):
        return sum(_largest_jolts(i, 12) for i in self.banks)
