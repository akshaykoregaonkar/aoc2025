from math import prod
from utils.union_find import UnionFind
import heapq

def _load_points():
    with open('input/day8.txt') as f:
        return [tuple(map(int, line.split(","))) for line in f]

def _straight_line_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def _pairwise_dist(points):
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            yield _straight_line_dist(points[i], points[j]), i, j


class Main:
    def __init__(self):
        self._points = _load_points()
        self._n = len(self._points)

    def part_one(self, k):
        uf = UnionFind(range(self._n))
        top3_heap = []

        for d, i, j in heapq.nsmallest(k, _pairwise_dist(self._points)):
            if uf.union(i, j):
                size = uf.size[uf.find(i)]
                if len(top3_heap) < 3:
                    heapq.heappush(top3_heap, size)
                elif size > top3_heap[0]:
                    heapq.heapreplace(top3_heap, size)
        return prod(top3_heap)

    def part_two(self):
        uf = UnionFind(range(len(self._points)))

        edges_heap = list(_pairwise_dist(self._points))
        heapq.heapify(edges_heap)

        while uf.count > 1:
            d, i, j = heapq.heappop(edges_heap)
            uf.union(i, j)

        return self._points[i][0] * self._points[j][0]
