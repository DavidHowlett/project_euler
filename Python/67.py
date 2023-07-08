"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.
"""
from functools import lru_cache

triangle = [[int(number) for number in line.split(' ')] for line in open('triangle.txt').read().split('\n')]
len_triangle = len(triangle)


@lru_cache
def max_score_at(x, y):
    if y >= len_triangle:
        return 0
    return triangle[y][x] + max(max_score_at(x, y + 1), max_score_at(x + 1, y + 1))


print(max_score_at(0, 0))
