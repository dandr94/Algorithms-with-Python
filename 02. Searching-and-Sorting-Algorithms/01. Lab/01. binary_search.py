"""
Implement an algorithm that finds the index of an element in a sorted array of integers in logarithmic time.
"""
from typing import List


def binary_search(target: int, array: List[int]) -> int:
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + end // 2
        mid_el = array[mid]

        if mid_el == target:
            return mid

        if mid_el > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


arr = [int(x) for x in input().split()]
tar = int(input())

print(binary_search(tar, arr))

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3461#0
