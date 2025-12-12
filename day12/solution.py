def parse_grids():
    with open("input/day12.txt") as f:
        return [
            (int(r), int(c), list(map(int, indices.split())))
            for line in f
            for size, indices in [line.split(":")]
            for r, _, c in [size.partition("x")]
        ]

class Main:
    def __init__(self):
        self._grids = parse_grids()

    def part_one(self):
        return sum(1 for row, col, idx in self._grids if sum(idx) * 9 <= row * col)
