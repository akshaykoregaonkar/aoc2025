from collections import defaultdict

def _load_grid():
    with open("input/day7.txt") as f:
        return [list(line.rstrip("\n")) for line in f]

class Main:
    def __init__(self):
        self._grid = _load_grid()
        self._start = self._grid[0].index('S')

    def part_one(self):
        grid, start = self._grid, self._start
        beams = {start}
        split_count = 0
        for i in range(1, len(grid)):
            next_beams = set()
            for b in beams:
                if grid[i][b] == '^':
                    next_beams.add(b - 1)
                    next_beams.add(b + 1)
                    split_count += 1
                else:
                    next_beams.add(b)
            beams = next_beams

        return split_count

    def part_two(self):
        grid, start = self._grid, self._start
        # store count of previous paths that reach each beam
        beams = {start: 1}

        for r in range(1, len(grid)):
            next_beams = defaultdict(int)
            for b, paths in beams.items():
                if grid[r][b] == '^':
                    next_beams[b - 1] += paths
                    next_beams[b + 1] += paths
                else:
                    next_beams[b] = next_beams.get(b, 0) + paths
            beams = next_beams

        return sum(beams.values())
