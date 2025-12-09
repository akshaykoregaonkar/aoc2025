import matplotlib.pyplot as plt
from itertools import combinations
from shapely import Polygon, box

def _load_red_tiles():
    with open('input/day9.txt') as f:
        return [tuple(map(int, line.split(","))) for line in f]

def _quick_shape_with_lines(pts, start_v_down=None, start_h_left=None, start_v_up=None, largest_rect=None):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]

    plt.figure(figsize=(12, 12))

    plt.fill(xs, ys, alpha=0.3, facecolor='lightblue', edgecolor='black', linewidth=1)
    plt.plot(xs, ys, color='black', linewidth=1)
    plt.scatter(xs[:-1], ys[:-1], s=20, color='red')

    if start_v_down is not None and start_h_left is not None and start_v_up is not None:
        plt.plot([start_v_down[0], start_v_down[0]], [start_v_down[1], max(ys)], color='orange', linewidth=2)
        plt.plot([min(xs), start_h_left[0]], [start_h_left[1], start_h_left[1]], color='orange', linewidth=2)
        plt.plot([start_v_up[0], start_v_up[0]], [min(ys), start_v_up[1]], color='orange', linewidth=2)

    if largest_rect is not None:
        (x_min, y_min), (x_max, y_max) = largest_rect
        rect_xs = [x_min, x_min, x_max, x_max, x_min]
        rect_ys = [y_min, y_max, y_max, y_min, y_min]
        plt.plot(rect_xs, rect_ys, color='green', linewidth=2, label='Largest rectangle')
        plt.legend()

    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.show()


def _largest_rect_in_polygon(pts):
    poly = Polygon(pts)
    max_area = 0
    best_rect = None

    for (x1, y1), (x2, y2) in combinations(pts, 2):
        rect_size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if rect_size < max_area:
            continue

        rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if poly.contains(rect):
            max_area = max(max_area, rect_size)
            best_rect = ((rect.bounds[0], rect.bounds[1]), (rect.bounds[2], rect.bounds[3]))
    return max_area, best_rect


class Main:
    def __init__(self):
        self._red_tiles = _load_red_tiles()

    def part_one(self):
        max_area = 0
        tiles = self._red_tiles
        n = len(tiles)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = tiles[i]
                p2 = tiles[j]
                area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1] +1))
                if area > max_area:
                    max_area = area
        return max_area

    """
    used matplot lib to plot the shape and then drew lines to create rectangle - see day09/part_two.png
    """
    def part_two(self):
        # manual approach:
        # self._quick_shape_with_lines(self._red_tiles)
        # self._quick_shape_with_lines(self._red_tiles, down, left, up)

        # found better solution using shapely on reddit that can just check if a shape is within a polygon
        max_area, best_rect =  _largest_rect_in_polygon(self._red_tiles)
        # can plot this out see day09/part_two_shapely.png
        #_quick_shape_with_lines(self._red_tiles, largest_rect=best_rect)
        return max_area
