"""
Write a program that finds the sum of all elements in an integer array.
Use recursion.
"""

from typing import List


def calculate(nums: List[int], index: int) -> int:
    current_element = nums[index]
    last_element = len(nums) - 1

    if index == last_element:  # Bottom for when recursion should stop
        return current_element

    next_element = index + 1

    return current_element + calculate(nums, next_element)


"""
1. Taking input as string with spaces;
Example - 1 2 3 4
2. Converting the input into list with .split() function;
3. Traversing the list and converting every str number into int.
"""
nums_input = [int(num) for num in input().split()]

# Asserting the result before printing it
expected_result = 10

result = calculate(nums_input, 0)

assert result == expected_result

# If all good prints the result
print(result)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#0
