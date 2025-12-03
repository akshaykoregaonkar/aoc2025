def _load_banks():
    with open("input/day3.txt") as f:
        return [[int(d) for d in line.strip()] for line in f]


def _largest_jolts_greedy(bank, k=2):
    stack = []
    n = len(bank)
    to_remove = n - k

    # greedy stack - remove any smaller batteries so top k are ordered and largest
    for battery in bank:
        while stack and stack[-1] < battery and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append(battery)

    return int("".join(map(str, stack[:k])))


def _largest_jolts_slicing(bank, k=2):
    result = []
    start = 0
    n = len(bank)

    # get max digit after current largest and until sub-array that has enough digits left to complete k
    for i in range(k):
        end = n - (k - len(result)) + 1
        max_digit = max(bank[start:end])
        result.append(max_digit)
        start = bank.index(max_digit, start) + 1
    return int("".join(map(str, result)))


class Main:
    def __init__(self):
        self.banks = _load_banks()

    def part_one_greedy(self):
        return sum(_largest_jolts_greedy(i) for i in self.banks)

    def part_two_greedy(self):
        return sum(_largest_jolts_greedy(i, 12) for i in self.banks)

    def part_one_slicing(self):
        return sum(_largest_jolts_slicing(i) for i in self.banks)

    def part_two_slicing(self):
        return sum(_largest_jolts_slicing(i, 12) for i in self.banks)
