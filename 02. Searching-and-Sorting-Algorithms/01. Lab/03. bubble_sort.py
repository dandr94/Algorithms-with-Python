"""
Write an implementation of Bubble Sort.
You should read an array of integers and sort them.
"""

from typing import List

from helpers.time_decorator import timing


@timing
def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


numbers = [int(x) for x in input().split()]
print(*bubble_sort(numbers), sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3461#2
