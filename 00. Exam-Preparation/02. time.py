"""You will be given two sequences of integers representing two timeline versions. You need to extract from both
sequences the single correct timeline that can be retrieved by finding the longest subsequence of equal integers from
both timelines and also finding its length."""
from collections import deque
from typing import List, Deque


def lcs(first: List[str], second: List[str]) -> List[List[int]]:
    rows = len(first_timeline) + 1
    cols = len(second_timeline) + 1

    dp = [[0] * cols for _ in range(rows)]

    for r in range(1, rows):
        for c in range(1, cols):
            if first[r - 1] == second[c - 1]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    return dp


def reconstruct_path(first: List[str], second: List[str], dp: List[List[int]]) -> Deque[str]:
    result = deque()

    row = len(first)
    col = len(second)

    while row > 0 and col > 0:
        if first_timeline[row - 1] == second_timeline[col - 1]:
            result.appendleft(first_timeline[row - 1])
            row -= 1
            col -= 1

        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return result


first_timeline = [x for x in input().split()]
second_timeline = [x for x in input().split()]

dp = lcs(first_timeline, second_timeline)

path = reconstruct_path(first_timeline, second_timeline, dp)

print(*path, sep=' ')
print(dp[-1][-1])

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3474#1
