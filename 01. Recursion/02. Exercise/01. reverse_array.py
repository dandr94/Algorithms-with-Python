"""
Write a program that reverses and prints an array. Use recursion.
"""
from typing import List


def reverse(index: int, arr: List[str]) -> None:
    if index == len(arr) // 2:
        return

    left_el = index
    right_el = len(arr) - 1 - index

    arr[left_el], arr[right_el] = arr[right_el], arr[left_el]

    reverse(index + 1, arr)


arr = input().split()

reverse(0, arr)

print(' '.join(arr))

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3460#0
