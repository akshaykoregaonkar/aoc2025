def _load_puzzle():
    with open("input/day11.txt") as f:
        return {k: v.split() for k, v in (line.split(":", 1) for line in f)}

def _count_paths(mapping, start, dac=None, fft=None):
    memo = {}

    def dfs(node, found_dac, found2_fft):
        key = (node, found_dac, found2_fft)
        if key in memo:
            return memo[key]

        next_node = mapping.get(node, [])

        found_dac = found_dac or (node == dac)
        found2_fft = found2_fft or (node == fft)

        if next_node == ["out"]:
            if (dac is None or fft is None) or (found_dac and found2_fft):
                memo[key] = 1
            else:
                memo[key] = 0
            return memo[key]

        total = sum(dfs(node, found_dac, found2_fft) for node in next_node)

        memo[key] = total
        return total

    return dfs(start, False, False)


class Main:
    def __init__(self):
        self.puzzle = _load_puzzle()

    def part_one(self):
        return _count_paths(self.puzzle, start="you")

    def part_two(self):
        return _count_paths(self.puzzle, start="svr", dac="dac", fft="fft")
