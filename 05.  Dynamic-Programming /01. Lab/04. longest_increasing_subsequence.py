"""
Let’s have a sequence of numbers S = {a1, a2, … an}.
An increasing subsequence is a sequence of numbers within S where each number is larger than the previous.
We do not change the relative positions of the numbers, e.g. we do not move smaller elements to the left to obtain longer sequences.
If several sequences with equal length exist, find the left-most of them
"""
from collections import deque

nums = [int(x) for x in input().split()]

size = [0] * len(nums)
size[0] = 1
parent = [None] * len(nums)

best_index = 0
best_size = 1

for current in range(1, len(nums)):
    current_number = nums[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]

        if prev_number >= current_number:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_index = current

result = deque()

while best_index is not None:
    result.appendleft(nums[best_index])
    best_index = parent[best_index]

print(*result, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3471#3
