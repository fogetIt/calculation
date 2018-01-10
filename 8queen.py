# -*- coding: utf-8 -*-
# @Date:   2018-01-09 10:03:08
# @Last Modified time: 2018-01-09 10:32:23
"""
8 皇后问题
"""
from __future__ import division


def main():
    x1, x2, x3, x4, x5, x6, x7, x8 = 1, 2, 3, 4, 5, 6, 7, 8
    for y1 in range(1, 9):
        for y2 in range(1, 9):
            if (
                y2 != y1
                and abs(y2 - y1) / abs(x2 - x1) != 1
            ):
                for y3 in range(1, 9):
                    if (
                        y3 != y2
                        and y3 != y1
                        and abs(y3 - y2) / abs(x3 - x2) != 1
                        and abs(y3 - y1) / abs(x3 - x1) != 1
                    ):
                        for y4 in range(1, 9):
                            if (
                                y4 != y3
                                and y4 != y2
                                and y4 != y1
                                and abs(y4 - y3) / abs(x4 - x3) != 1
                                and abs(y4 - y2) / abs(x4 - x2) != 1
                                and abs(y4 - y1) / abs(x4 - x1) != 1
                            ):
                                for y5 in range(1, 9):
                                    if (
                                        y5 != y4
                                        and y5 != y3
                                        and y5 != y2
                                        and y5 != y1
                                        and abs(y5 - y4) / abs(x5 - x4) != 1
                                        and abs(y5 - y3) / abs(x5 - x3) != 1
                                        and abs(y5 - y2) / abs(x5 - x2) != 1
                                        and abs(y5 - y1) / abs(x5 - x1) != 1
                                    ):
                                        for y6 in range(1, 9):
                                            if (
                                                y6 != y5
                                                and y6 != y4
                                                and y6 != y3
                                                and y6 != y2
                                                and y6 != y1
                                                and abs(y6 - y5) / abs(x6 - x5) != 1
                                                and abs(y6 - y4) / abs(x6 - x4) != 1
                                                and abs(y6 - y3) / abs(x6 - x3) != 1
                                                and abs(y6 - y2) / abs(x6 - x2) != 1
                                                and abs(y6 - y1) / abs(x6 - x1) != 1
                                            ):
                                                for y7 in range(1, 9):
                                                    if (
                                                        y7 != y6
                                                        and y7 != y5
                                                        and y7 != y4
                                                        and y7 != y3
                                                        and y7 != y2
                                                        and y7 != y1
                                                        and abs(y7 - y6) / abs(x7 - x6) != 1
                                                        and abs(y7 - y5) / abs(x7 - x5) != 1
                                                        and abs(y7 - y4) / abs(x7 - x4) != 1
                                                        and abs(y7 - y3) / abs(x7 - x3) != 1
                                                        and abs(y7 - y2) / abs(x7 - x2) != 1
                                                        and abs(y7 - y1) / abs(x7 - x1) != 1
                                                    ):
                                                        for y8 in range(1, 9):
                                                            if (
                                                                y8 != y7
                                                                and y8 != y6
                                                                and y8 != y5
                                                                and y8 != y4
                                                                and y8 != y3
                                                                and y8 != y2
                                                                and y8 != y1
                                                                and abs(y8 - y7) / abs(x8 - x7) != 1
                                                                and abs(y8 - y6) / abs(x8 - x6) != 1
                                                                and abs(y8 - y5) / abs(x8 - x5) != 1
                                                                and abs(y8 - y4) / abs(x8 - x4) != 1
                                                                and abs(y8 - y3) / abs(x8 - x3) != 1
                                                                and abs(y8 - y2) / abs(x8 - x2) != 1
                                                                and abs(y8 - y1) / abs(x8 - x1) != 1
                                                            ):
                                                                print(
                                                                    (x1, y1),
                                                                    (x2, y2),
                                                                    (x3, y3),
                                                                    (x4, y4),
                                                                    (x5, y5),
                                                                    (x6, y6),
                                                                    (x7, y7),
                                                                    (x8, y8),
                                                                )


if __name__ == '__main__':
    main()
