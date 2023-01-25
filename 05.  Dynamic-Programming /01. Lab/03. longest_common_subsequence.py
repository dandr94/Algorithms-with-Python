"""
Considering two sequences S1 and S2, the longest common subsequence is a sequence that is a subsequence of both S1 and S2.
For instance, if we have two strings (sequences of characters),
"abc" and "adb", the LCS is "ab" – it is a subsequence of both sequences,
and it is the longest (there are two other subsequences – "a" and "b").
"""
from collections import deque

first_str = input()
second_str = input()

rows = len(first_str) + 1
cols = len(second_str) + 1

dp = [[0] * cols for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first_str[row - 1] == second_str[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])


lcs = dp[rows - 1][cols - 1]

print(lcs)

# row = rows - 1
# col = cols - 1
#
# result = deque()
#
# while row > 0 and col > 0:
#     if first_str[row - 1] == second_str[col - 1]:
#         result.appendleft(first_str[row - 1])
#         row -= 1
#         col -= 1
#
#     elif dp[row - 1][col] > dp[row][col - 1]:
#         row -= 1
#     else:
#         col -= 1
#
# print(result)



# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3471#2