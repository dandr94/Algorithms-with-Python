"""
Sort an array of elements using the famous merge sort.
"""
from typing import List

from helpers.time_class import Timeit


def merge(left: List[int], right: List[int]) -> List[int]:
    result = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    result_idx = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result[result_idx] = left[left_index]
            left_index += 1
        else:
            result[result_idx] = right[right_index]
            right_index += 1

        result_idx += 1

    while left_index < len(left):
        result[result_idx] = left[left_index]
        left_index += 1
        result_idx += 1

    while right_index < len(right):
        result[result_idx] = right[right_index]
        right_index += 1
        result_idx += 1

    return result


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums

    mid_index = len(nums) // 2
    left = nums[:mid_index]
    right = nums[mid_index:]

    return merge(merge_sort(left), merge_sort(right))


numbers = [int(x) for x in input().split()]

print(*merge_sort(numbers), sep=' ')

with Timeit(merge_sort) as f:
    res = f(numbers)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3461#5
