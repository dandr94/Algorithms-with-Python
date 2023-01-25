"""
Given a matrix of N by M cells filled with positive integers,
find the path from top left to bottom right with the highest sum of cells by moving only down or right.
"""
from collections import deque

rows = int(input())
cols = int(input())

matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col] + matrix[row][col], dp[row][col - 1] + matrix[row][col])

r = rows - 1
c = cols - 1

result = deque()

while r > 0 and c > 0:
    result.appendleft([r, c])

    if dp[r][c - 1] >= dp[r - 1][c]:
        c -= 1
    else:
        r -= 1

for i in range(r, 0, - 1):
    result.appendleft([i, c])

for i in range(c, 0, - 1):
    result.appendleft([r, i])

result.appendleft([0, 0])

print(*result, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3471#1
