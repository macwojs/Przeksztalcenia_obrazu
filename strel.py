import numpy as np
from bresenham import bresenham


def strel_line(length, deg):
    if length >= 1:
        th = deg * np.pi / 180
        x = round((length - 1) / 2 * np.cos(th))
        y = -round((length - 1) / 2 * np.sin(th))

        points = list(bresenham(int(-x), int(-y), int(x), int(y)))

        points_x = [point[0] for point in points]
        col_n = int(2 * max([abs(point_x) for point_x in points_x]) + 1)
        columns = ([point_x + max([abs(point_x) for point_x in points_x]) for point_x in points_x])

        points_y = [point[1] for point in points]
        row_n = int(2 * max([abs(point_y) for point_y in points_y]) + 1)
        rows = ([point_y + max([abs(point_y) for point_y in points_y]) for point_y in points_y])

        ind = []
        strel = np.zeros((row_n, col_n))
        for x in zip(rows, columns):
            ind.append(np.ravel_multi_index((int(x[0]), int(x[1])), (row_n, col_n)))
        strel.reshape(-1)[ind] = 1

    return strel
