from pathlib import Path


def _load_instructions():
    input_file = Path(__file__).parent.parent / "input" / "day1.txt"
    with open(input_file) as f:
        return [(line[0], int(line[1:])) for line in map(str.strip, f) if line]


class Main:
    DIAL = 100

    def __init__(self):
        self._instructions = _load_instructions()

    def _move(self, pos, dist, direction):
        if direction == "L":
            return (pos - dist) % self.DIAL
        else:
            return (pos + dist) % self.DIAL

    def part_one(self):
        pos, password = 50, 0

        for direction, dist in self._instructions:
            pos = self._move(pos, dist % self.DIAL, direction)
            if pos == 0:
                password += 1
        return password

    def part_two(self):
        pos, password = 50, 0

        for direction, dist in self._instructions:
            prev = pos
            # count multiple loops (e.g. 218 means we pass dial twice and remainder 18 once)
            password += dist // self.DIAL
            rem = dist % self.DIAL

            if direction == "L":
                wrapped = rem > prev
                pos = self._move(pos, rem, direction)

                if (wrapped and prev > 0) or pos == 0:
                    password += 1
            else:
                wrapped = prev + rem >= self.DIAL
                pos = self._move(pos, rem, direction)

                if wrapped:
                    password += 1
        return password
