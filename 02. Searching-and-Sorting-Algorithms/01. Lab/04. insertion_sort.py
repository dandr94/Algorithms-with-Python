"""
Write an implementation of Insertion Sort.
You should read an array of integers and sort them.
"""
from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        for j in range(i, 0, - 1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

    return nums


numbers = [int(x) for x in input().split()]
print(*insertion_sort(numbers), sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3461#3
