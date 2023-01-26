"""
Given a list of strings, write a program that returns the longest string chain that can be built from those strings.
A string chain is defined as follows: subsequence of a given sequence in which the subsequence's elements are in sorted order (string length),
lowest to highest, and in which the subsequence is as long as possible.
If several sequences with equal length exist, find the left-most of them.
"""
from collections import deque
from typing import Deque, List


def longest_string_chain(words: List[str]) -> Deque[str]:
    size = [0] * len(words)
    prev = [None] * len(words)
    result = deque()

    best_size = 0
    best_index = 0

    for i in range(len(words)):
        cur_word = words[i]
        cur_size = 1
        parent = None

        for j in range(i - 1, -1, - 1):
            prev_word = words[j]

            if len(prev_word) >= len(cur_word):
                continue

            if size[j] + 1 >= cur_size:
                cur_size = size[j] + 1
                parent = j

        size[i] = cur_size
        prev[i] = parent

        if cur_size > best_size:
            best_size = cur_size
            best_index = i

    while best_index is not None:
        result.appendleft(words[best_index])
        best_index = prev[best_index]

    return result


words = [x for x in input().split()]

res = longest_string_chain(words)

print(*res, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3473#4
