"""
Write a program that finds all the differences between two strings.
You have to determine the smallest set of deletions and insertions to make the first string equal to the second.
Finally, you have to print the count of the minimum insertions and deletions.
"""


def word_differences(first: str, second: str) -> int:
    dp = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

    for i in range(len(first) - 1, -1, -1):
        for j in range(len(second) - 1, -1, -1):
            dp[i][j] = 1 + dp[i + 1][j + 1] if first[i] == second[j] else max(dp[i + 1][j], dp[i][j + 1])

    return len(first) - dp[0][0] + len(second) - dp[0][0]


# def word_differences(first: str, second: str) -> int:
#     dp = [[i for i in range(len(second) + 1)]] + [[i] + [0] * (len(second)) for i in range(1, len(first) + 1)]
#
#     for i in range(len(first)):
#         for j in range(len(second)):
#             dp[i + 1][j + 1] = dp[i][j] if first[i] == second[j] else min(dp[i + 1][j], dp[i][j + 1]) + 1
#
#     return dp[-1][-1]


first_str = input()
second_str = input()

res = word_differences(first_str, second_str)

print(f'Deletions and Insertions: {res}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3473#1
