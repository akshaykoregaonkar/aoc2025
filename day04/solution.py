MAX_ROLLS_FORKLIFT = 3
NEIGHBOURS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def _load_puzzle():
    with open("input/day4.txt") as f:
        return [list(line.strip()) for line in f]


class Main:
    def __init__(self):
        self._puzzle = _load_puzzle()
        self._rows = len(self._puzzle)
        self._cols = len(self._puzzle[0])

    def part_one(self):
        removed_rolls = 0
        puzzle = self._puzzle
        for r, row in enumerate(puzzle):
            for c, col in enumerate(row):
                if col == '@' and self._can_access(r, c):
                    removed_rolls += 1
        return removed_rolls

    def part_two(self):
        result = 0
        puzzle = self._puzzle
        while True:
            removed_rolls = 0
            for r, row in enumerate(puzzle):
                for c, col in enumerate(row):
                    if col == '@' and self._can_access(r, c):
                        removed_rolls += 1
                        result += 1
                        puzzle[r][c] = '.'

            if removed_rolls == 0:
                break

        return result

    def _can_access(self, r: int, c: int):
        count = 0
        puzzle, rows, cols = self._puzzle, self._rows, self._cols
        for dr, dc in NEIGHBOURS:
            nr = dr + r
            nc = dc + c

            if 0 <= nr < rows and 0 <= nc < cols:
                if puzzle[nr][nc] == '@':
                    count += 1
                    if count > MAX_ROLLS_FORKLIFT:
                        return False
        return True
