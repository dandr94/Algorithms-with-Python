"""
Implement a recursive algorithm to solve the "8 Queens" puzzle.
Write a program to find all possible placements of 8 chess queens on a chessboard so
that no two queens can attack each other (on a row, column, or diagonal).
"""
from typing import List


def valid_place(row: int, col: int, rows: set, cols: set, l_d: set, r_d: set) -> bool:
    if row in rows or col in cols or (row - col) in l_d or (row + col) in r_d:
        return False

    return True


def place_queen(row: int, col: int, board: List[List[str]], rows: set, cols: set, l_d: set, r_d: set) -> None:
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    l_d.add(row - col)
    r_d.add(row + col)


def remove_queen(row: int, col: int, board: List[List[str]], rows: set, cols: set, l_d: set, r_d: set) -> None:
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    l_d.remove(row - col)
    r_d.remove(row + col)


def print_board(board: List[List[str]]) -> None:
    [print(' '.join(r)) for r in board]
    print()


def place_queens(row: int, board: List[List[str]], rows: set, cols: set, l_d: set, r_d: set) -> None:
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if valid_place(row, col, rows, cols, l_d, r_d):
            place_queen(row, col, board, rows, cols, l_d, r_d)
            place_queens(row + 1, board, rows, cols, l_d, r_d)
            remove_queen(row, col, board, rows, cols, l_d, r_d)


n = 8
b = [['-'] * n for _ in range(n)]

place_queens(0, b, set(), set(), set(), set())

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#5
