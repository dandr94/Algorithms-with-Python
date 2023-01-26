"""
Write a program that finds the binomial coefficient  for given non-negative integers n and k.
The coefficient can be found recursively by adding the two numbers.
However, this leads to calculating the same coefficient multiple times (a problem that also occurs when solving the Fibonacci problem recursively).
Use memoization to improve performance.
"""


def bc(n, k, memo):
    key = f'{n} {k}'

    if key in memo:
        return memo[key]

    if n == 0 or k == 0 or n == k:
        return 1

    result = bc(n - 1, k - 1, memo) + bc(n - 1, k, memo)

    memo[key] = result

    return result


n = int(input())
k = int(input())

res = bc(n, k, {})

print(res)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3473#0
