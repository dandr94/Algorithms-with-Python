"""
Sort an array of elements using the famous quicksort.
"""
from typing import List
from helpers.time_class import Timeit


def quick_sort(start: int, end: int, nums: List[int]) -> List[int]:
    if start >= end:
        return nums

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1

        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]

    quick_sort(start, right - 1, nums)
    quick_sort(left, end, nums)

    return nums


numbers = [int(x) for x in input().split()]
s = 0
e = len(numbers) - 1

print(*quick_sort(s, e, numbers), sep=' ')

with Timeit(quick_sort) as f:
    result = f(s, e, numbers)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3461#4
