"""
Write a dynamic programming solution for finding nth Fibonacci members.
    • F0 = 0
    • F1 = 1
"""
from helpers.time_decorator import timing
from helpers.time_class import Timeit


# @timing
# def fibonacci(n):
#     if n <= 2:
#         return 1
#
#     a, b = 0, 1
#
#     for i in range(n):
#         a, b = b, a + b
#
#     return a


def fibonacci(n, memo):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result

    return result


n = int(input())
print(fibonacci(n, {}))

with Timeit(fibonacci) as f:
    r = f(n, {})

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3471#0
