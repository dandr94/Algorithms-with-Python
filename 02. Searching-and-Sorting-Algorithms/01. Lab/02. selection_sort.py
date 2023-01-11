"""
Write an implementation of Selection Sort.
You should read an array of integers and sort them.
"""
from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        min_idx = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


numbers = [int(x) for x in input().split()]
print(*selection_sort(numbers), sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3461#1
