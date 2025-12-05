def _load_inventory():
    with open("input/day5.txt") as f:
        parts = f.read().strip().split("\n\n")
        ranges = tuple(
            tuple(map(int, line.split("-")))
            for line in parts[0].splitlines()
        )

        ingredients = [int(line) for line in parts[1].splitlines()]
    return ranges, ingredients


def _merge_ranges(_ranges):
    sorted_ranges = sorted(_ranges, key=lambda x: x[0])
    merged = []

    for start, end in sorted_ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return tuple(map(tuple, merged))


def _binary_search(i, ranges):
    left, right = 0, len(ranges) - 1
    candidate_idx = -1

    while left <= right:
        mid = (left + right) // 2
        start, end = ranges[mid]

        if start <= i:
            candidate_idx = mid
            left = mid + 1
        else:
            right = mid - 1

    if candidate_idx == -1:
        return False

    start, end = ranges[candidate_idx]
    return start <= i <= end


class Main:
    def __init__(self):
        self._ranges, self._ingredients = _load_inventory()
        self._merged_ranges = _merge_ranges(self._ranges)

    def part_one(self):
        return sum(
            _binary_search(i, self._merged_ranges)
            for i in self._ingredients
        )


    def part_two(self):
        return sum(end - start + 1 for start, end in self._merged_ranges)
