"""
A zigzag sequence is one that alternately increases and decreases. More formally, such a sequence has to comply with one of the two rules below:
    1) Every even element is smaller than its neighbors and every odd element is larger than its neighbors, or
    2) Every odd element is smaller than its neighbors and every even element is larger than its neighbors
1 3 2 is a zigzag sequence, but 1 2 3 is not. Any sequence of one or two elements is zigzag.
Find the longest zigzag subsequence in a given sequence.
"""
from collections import deque
from typing import List, Deque


def lis(nums: List[int]) -> Deque[int]:
    dp = [[0] * len(nums) for _ in range(2)]
    dp[0][0] = dp[1][0] = 1

    parent = [[None] * len(nums) for _ in range(2)]

    result = deque()

    best_size, best_row, best_col = 0, 0, 0

    for i in range(1, len(nums)):
        cur_number = nums[i]

        for j in range(i - 1, -1, -1):
            prev_number = nums[j]

            if cur_number > prev_number and dp[1][j] + 1 >= dp[0][i]:
                dp[0][i], parent[0][i] = dp[1][j] + 1, j

            if cur_number < prev_number and dp[0][j] + 1 >= dp[1][i]:
                dp[1][i], parent[1][i] = dp[0][j] + 1, j

        if dp[0][i] > best_size:
            best_size, best_row, best_col = dp[0][i], 0, i

        if dp[1][i] > best_size:
            best_size, best_row, best_col = dp[1][i], 1, i

    while best_col is not None:
        result.appendleft(nums[best_col])
        best_col = parent[best_row][best_col]
        best_row = 1 if best_row == 0 else 0

    return result


nums = [int(x) for x in input().split()]

res = lis(nums)

print(*res, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3473#5
