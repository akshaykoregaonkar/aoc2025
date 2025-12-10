from collections import deque
import pulp

def _load_machines():
    machines = []

    with open('input/day10.txt') as f:
        for machine in f:
            start, end = machine.index('[') + 1, machine.index(']')
            lights = [1 if c == "#" else 0 for c in machine[start:end]]

            start, end = end + 1, machine.index('{')
            button_str = machine[start:end].replace('(','').split(')')
            buttons = [tuple(map(int, b.split(',')))
                       for b in button_str if b.strip()]

            start, end = machine.index('{') + 1, machine.index('}')
            joltage = list(map(int, machine[start:end].split(',')))

            machines.append((lights, buttons, joltage))

    return machines

def _get_mask(buttons):
    mask = 0
    for i in buttons:
        mask |= 1 << i
    return mask

def _shortest_light_sequence(expected_lights, buttons):
    start_lights = [0] * len(expected_lights)

    start_mask = _get_mask([i for i, v in enumerate(start_lights) if v == 1])
    goal_mask  = _get_mask([i for i, v in enumerate(expected_lights) if v == 1])

    button_masks = [_get_mask(b) for b in buttons]

    queue = deque([(start_mask, [])])
    visited = {start_mask}

    while queue:
        state, path = queue.popleft()

        if state == goal_mask:
            return path

        for i, b_mask in enumerate(button_masks):
            next_state = state ^ b_mask
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [i]))

    return None

def _shortest_joltage_presses(joltage, buttons):
    n_counters = len(joltage)
    n_buttons = len(buttons)

    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer")
         for j in range(n_buttons)]

    prob = pulp.LpProblem()
    prob += pulp.lpSum(x)

    for i in range(n_counters):
        buttons_that_jolt = [j for j in range(n_buttons) if i in buttons]
        num_of_presses = pulp.lpSum(x[j] for j in buttons_that_jolt)
        prob += num_of_presses == joltage[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    return [int(v.value()) for v in x]


class Main:
    def __init__(self):
        self.machines = _load_machines()

    def part_one(self):
        return sum(len(_shortest_light_sequence(lights, buttons))
                   for lights, buttons, _ in self.machines)

    def part_two(self):
        return sum(sum(_shortest_joltage_presses(joltage, buttons))
                   for _, buttons, joltage in self.machines)
