"""
Let’s define a connected area in a matrix as an area of cells in which there is a path between every two cells.
Write a program to find all connected areas in a matrix.

Example:
    r = 4
    c = 9

    ---*---*-
    ---*---*-
    ---*---*-
    ----*-*--

    Total areas found: 3
    Area #1 at (0, 0), size: 13
    Area #2 at (0, 4), size: 10
    Area #3 at (0, 8), size: 5

"""
from typing import List


class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

    def __str__(self):
        return f'({self.row}, {self.col}), size: {self.size}'


def find_areas(row: int, col: int, matrix: List[List[str]]) -> int:
    if not is_valid_index(row, col, matrix):
        return 0

    if is_visited(row, col, matrix):
        return 0

    if is_wall(row, col, matrix):
        return 0

    matrix[row][col] = 'v'

    result = 1
    result += find_areas(row - 1, col, matrix)  # Up
    result += find_areas(row + 1, col, matrix)  # Down
    result += find_areas(row, col - 1, matrix)  # Left
    result += find_areas(row, col + 1, matrix)  # Right

    return result


def is_valid_index(row: int, col: int, matrix: List[List[str]]) -> bool:
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return False

    return True


def is_visited(row: int, col: int, matrix: List[List[str]]) -> bool:
    if matrix[row][col] == 'v':
        return True


def is_wall(row: int, col: int, matrix: List[List[str]]) -> bool:
    if matrix[row][col] == '*':
        return True


rows = int(input())
cols = int(input())
m = [list(input()) for _ in range(rows)]

areas = []

for r in range(rows):
    for c in range(cols):
        size = find_areas(r, c, m)
        if size != 0:
            areas.append(Area(r, c, size))


areas = sorted(areas, key=lambda x: (-x.size, x.row, x.col))

print(f'Total areas found: {len(areas)}')

for index, area in enumerate(areas):
    print(f'Area #{index + 1} at {area}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3460#3
