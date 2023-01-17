"""
given a matrix of letters of size N * M.
Two cells are neighbors if they share a common wall.
Write a program to find the connected areas of neighbor cells holding the same letter.
Display the total number of areas and the number of areas for each alphabetical letter (ordered by alphabetical order).
"""
from typing import List


def dfs(key: str,
        row: int,
        col: int,
        matrix: List[List[str]],
        visited: List[List[bool]]):

    if not is_valid_index(row, col, matrix):
        return

    if not is_same_key(key, row, col, matrix):
        return

    if is_visited(row, col, visited):
        return

    visited[row][col] = True

    dfs(key, row - 1, col, matrix, visited)
    dfs(key, row + 1, col, matrix, visited)
    dfs(key, row, col - 1, matrix, visited)
    dfs(key, row, col + 1, matrix, visited)


def is_visited(row: int,
               col: int,
               visited: List[List[bool]]) -> bool:

    if visited[row][col]:
        return True

    return False


def is_same_key(key: str,
                row: int,
                col: int,
                matrix: List[List[str]]) -> bool:

    if matrix[row][col] == key:
        return True

    return False


def is_valid_index(row: int,
                   col: int,
                   matrix: List[List[str]]) -> bool:

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return False

    return True


r = int(input())
c = int(input())

matrix = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
areas = {}
total_areas = 0

for row in range(r):
    for col in range(c):
        if not visited[row][col]:
            key = matrix[row][col]
            dfs(key, row, col, matrix, visited)
            if key not in areas:
                areas[key] = 0
            areas[key] += 1
            total_areas += 1

print(f'Areas: {total_areas}')

for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3463#0
