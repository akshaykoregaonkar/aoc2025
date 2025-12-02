from pathlib import Path


def load_ranges() -> list[tuple[int, int]]:
    path = Path(__file__).parent.parent / "input" / "day2.txt"
    return [
        tuple(map(int, product_range.split("-")))
        for product_range in Path(path).read_text().strip().split(",")
    ]


def _has_repeats_exact_half(i: int) -> bool:
    s = str(i)
    n = len(s)

    if n % 2 != 0:
        return False
    mid = n // 2
    chunk = s[:mid]
    return chunk * 2 == s


def _has_repeats_any_chunk(i: int) -> bool:
    s = str(i)
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            chunk = s[:size]
            if chunk * (n // size) == s:
                return True
    return False


class Main:
    def __init__(self):
        self.ranges = load_ranges()

    def part_one(self) -> int:
        return sum(
            i for first, last in self.ranges
            for i in range(first, last + 1)
            if _has_repeats_exact_half(i)
        )

    def part_two(self) -> int:
        return sum(
            i for first, last in self.ranges
            for i in range(first, last + 1)
            if _has_repeats_any_chunk(i)
        )