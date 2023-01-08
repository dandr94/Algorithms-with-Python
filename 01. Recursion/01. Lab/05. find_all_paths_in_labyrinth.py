"""
You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with 'e'.
•	Empty cells are marked with a dash '-'.
•	Walls are marked with a star '*'.
On the first line, you will receive the dimensions of the labyrinth. Next, you will receive the actual labyrinth.
The order of the paths does not matter.

Example:
    input:
            3
            3
            ---
            -*-
            --e

    output:
            RRDD
            DDRR

"""
from typing import List


def find_lab_paths(row: int, col: int, labyrinth: List[List[str]], direction: str, path: List[str]) -> None:
    if not is_valid_index(row, col, labyrinth):
        return

    if is_wall(row, col, labyrinth):
        return

    if is_visited(row, col, labyrinth):
        return

    path.append(direction)

    if reached_ending(row, col, labyrinth):
        print(''.join(path))
    else:
        labyrinth[row][col] = 'v'

        find_lab_paths(row - 1, col, labyrinth, 'U', path)  # Up
        find_lab_paths(row + 1, col, labyrinth, 'D', path)  # Down
        find_lab_paths(row, col - 1, labyrinth, 'L', path)  # Left
        find_lab_paths(row, col + 1, labyrinth, 'R', path)  # Right

        labyrinth[row][col] = '-'

    path.pop()


def is_valid_index(row: int, col: int, labyrinth: List[List[str]]) -> bool:
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        return False

    return True


def reached_ending(row: int, col: int, labyrinth: List[List[str]]) -> bool:
    if labyrinth[row][col] == 'e':
        return True


def is_wall(row: int, col: int, labyrinth: List[List[str]]) -> bool:
    if labyrinth[row][col] == '*':
        return True


def is_visited(row: int, col: int, labyrinth: List[List[str]]) -> bool:
    if labyrinth[row][col] == 'v':
        return True


r = int(input())
c = int(input())
lab = [list(input()) for _ in range(r)]

find_lab_paths(0, 0, lab, '', [])

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#4
