"""
Marinette has the ability to transform into Ladybug.
She is stuck on a grid.
Her initial location is in the top-left corner and tries to move to the bottom-right corner.
However, she can only move either down or right at any point in time.
Write a program that prints the number of all possible unique paths that Marinette can take to reach the bottom-right corner.

"""


def count_paths(row: int, col: int, rows: int, cols: int) -> int:
    if not is_valid_index(row, col, rows, cols):
        return 0

    if reached_ending(row, col, rows, cols):
        return 1

    result = 0

    result += count_paths(row, col + 1, rows, cols)
    result += count_paths(row + 1, col, rows, cols)

    return result


def is_valid_index(row: int, col: int, rows: int, cols: int) -> bool:
    if row >= rows or col >= cols:
        return False

    return True


def reached_ending(row: int, col: int, rows: int, cols: int) -> bool:
    if row == rows - 1 and col == cols - 1:
        return True


r = int(input())
c = int(input())

print(count_paths(0, 0, r, c))

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3460#2
