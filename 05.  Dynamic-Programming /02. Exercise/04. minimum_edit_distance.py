"""
We have two strings, s1 and s2. The goal is to obtain s2 from s1 by applying the following operations:
    • replace(i, x) – in s1, replaces the symbol at index  with the character x
    • insert(i, x) – in s1, inserts the character x at index i
    • delete(i) – from s1, removes the character at index i
We are only allowed to modify s1, s2 always stays unchanged. Each of the three operations has a certain cost associated with it (positive integer number).
Note: the cost of the replace(i, x) operation is 0 if it does not change the character.
The goal is to find the sequence of operations which will produce s2 from s1 with minimal cost.
"""
import pprint


def minimum_edit_distance(s1: str, s2: str) -> int:
    rows = len(s1) + 1
    cols = len(s2) + 1
    dp = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + delete_cost
    for i in range(1, cols):
        dp[0][i] = dp[0][i - 1] + insert_cost

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j - 1] if s1[i - 1] == s2[j - 1] else min(dp[i - 1][j - 1] + replacement_cost,
                                                                           dp[i][j - 1] + insert_cost,
                                                                           dp[i - 1][j] + delete_cost
                                                                           )

    return dp[-1][-1]


replacement_cost = int(input())
insert_cost = int(input())
delete_cost = int(input())
s1 = input()
s2 = input()

res = minimum_edit_distance(s1, s2)

print(f'Minimum edit distance: {res}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3473#3
