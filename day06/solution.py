# idea is to split numbers when all columns have a space at an index
def _space_by_columns(rows):
    result = []
    separators = [i for i in range(len(rows[0])) if all(r[i] == " " for r in rows)]

    for r in rows:
        row_splits = []
        start = 0
        for sep in separators:
            row_splits.append(r[start:sep])
            start = sep + 1
        row_splits.append(r[start:])
        result.append(row_splits)
    return result

def _load_data():
    with open("input/day6.txt") as f:
        rows = [line.rstrip("\n") for line in f]

    operations = rows[-1].split()
    cols = list(zip(*_space_by_columns(rows[:-1])))
    return cols, operations


def _cephalopod_col(col):
    max_len = max(map(len,col))

    output = []
    for i in range(max_len):
        digits = [num[i] for num in col if i < len(num)]
        output.append(int("".join(digits)))
    return output


class Main:
    def __init__(self):
        self.cols, self.operations = _load_data()

    @staticmethod
    def _apply(op, nums):
        if op == "*":
            result = 1
            for n in nums:
                result *= n
            return result
        return sum(nums)

    def part_one(self):
        total = 0
        ops, cols = self.operations, self.cols
        for op, col in zip(ops, cols):
            nums = [int(x) for x in col]
            total += self._apply(op, nums)
        return total

    def part_two(self):
        total = 0
        ops, cols = self.operations, self.cols
        for op, col in zip(ops, cols):
            nums = _cephalopod_col(col)
            total += self._apply(op, nums)
        return total
