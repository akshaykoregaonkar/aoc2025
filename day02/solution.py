def load_ranges() -> list[tuple[int, int]]:
    with open("input/day2.txt") as f:
        return [
            tuple(map(int, r.split("-")))
            for r in f.read().strip().split(",")
        ]


# generate possible chunks between ranges instead of checking each individual number is invalid
def _generate_repeating_numbers(start: int, end: int, part_one: bool = False) -> int:
    results = set()

    min_len = len(str(start))
    max_len = len(str(end))

    for length in range(min_len, max_len + 1):
        if part_one:
            if length % 2 != 0:
                continue
            chunk_sizes = [length // 2]
        else:
            chunk_sizes = [c for c in range(1, length // 2 + 1) if length % c == 0]

        for chunk_size in chunk_sizes:
            repeats = length // chunk_size

            start_chunk = 10 ** (chunk_size - 1)
            end_chunk = 10 ** chunk_size
            for c in range(start_chunk, end_chunk):
                chunk = str(c)
                num = int(chunk * repeats)
                if start <= num <= end:
                    results.add(num)

    return sum(results)


class Main:
    def __init__(self):
        self.ranges = load_ranges()

    def part_one(self) -> int:
        return sum(_generate_repeating_numbers(start, end, part_one=True) for start, end in self.ranges)

    def part_two(self) -> int:
        return sum(_generate_repeating_numbers(start, end) for start, end in self.ranges)
