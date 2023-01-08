"""
Each member of the Fibonacci sequence is calculated from the sum of the two previous members.
The first two elements are 1, 1.
Therefore, the sequence goes as 1, 1, 2, 3, 5, 8, 13, 21, 34…
The following sequence can be generated with an array, but that’s easy, so your task is to implement it recursively.

"""

memo = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


n_fib = int(input()) + 1

print(fib(n_fib))

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#6
