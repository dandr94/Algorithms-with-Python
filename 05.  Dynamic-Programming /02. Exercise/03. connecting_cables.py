"""
We are in a rectangular room. On opposite sides of the room, there are sets of n cables (n < 1000).
The cables are indexed from 1 to n.
On each side of the room, there is a permutation of the cables, e.g. on one side we always have ordered {1, 2, 3, 4, 5}
and on the other side, we have some permutation {5, 1, 3, 4, 2}.
We are trying to connect each cable from one side with the corresponding cable on the other side – connect 1 with 1, 2 with 2, etc.
The cables are straight and should not overlap!
The task is to find the maximum number of pairs we can connect given the restrictions above.
"""
from typing import List


def connecting_cables(cables: List[int]) -> int:
    size = len(cables) + 1

    positions = [p for p in range(1, size)]

    dp = [[0] * size for _ in range(size)]

    for row in range(1, size):
        for col in range(1, size):
            dp[row][col] = dp[row][col] = dp[row - 1][col - 1] + 1 if cables[row - 1] == positions[col - 1] else max(
                dp[row - 1][col], dp[row][col - 1])

    return dp[size - 1][-1]


cables = [int(x) for x in input().split()]

res = connecting_cables(cables)

print(f'Maximum pairs connected: {res}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3473#2
