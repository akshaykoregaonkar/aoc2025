from collections import defaultdict
from math import prod
from utils.union_find import UnionFind


def _load_points():
    with open('input/day8.txt') as f:
        return [tuple(map(int, line.split(","))) for line in f]

def _straight_line_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def _sort_by_distance(points):
    n = len(points)

    pairs = [
        (i, j, _straight_line_dist(points[i], points[j]))
        for i in range(n) for j in range(i + 1, n)
    ]
    pairs.sort(key=lambda x: x[2])
    return pairs


class Main:
    def __init__(self):
        self._points = _load_points()
        self._points_sorted = _sort_by_distance(self._points)

    def part_one(self, num_of_connections: int) -> int:
        uf = UnionFind(range(len(self._points)))

        for p1, p2, _ in self._points_sorted[:num_of_connections]:
            uf.union(p1, p2)

        circuits = self._get_disjoint_sets(uf)

        top_3_circuit_sizes = sorted((len(s) for s in circuits.values()), reverse=True)[:3]

        return prod(top_3_circuit_sizes)

    def part_two(self):
        uf = UnionFind(range(len(self._points)))
        for p1, p2, _ in self._points_sorted:
            uf.union(p1, p2)
            if uf.count == 1:
                return self._points[p1][0] * self._points[p2][0]
        return -1

    def _get_disjoint_sets(self, uf):
        circuits = defaultdict(list)
        for i in range(len(self._points)):
            root = uf.find(i)
            circuits[root].append(i)
        return circuits

