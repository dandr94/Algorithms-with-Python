"""
Write a program that calculates the recursively factorial of a given number.
"""


def factorial(num: int) -> int:
    if num == 0:  # Bottom for our recursion
        return 1

    return num * factorial(num - 1)


# Asserting the result before printing it

expected_result = 120

result = factorial(5)

assert result == expected_result

# If all good prints the result
print(factorial(5))

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#1
