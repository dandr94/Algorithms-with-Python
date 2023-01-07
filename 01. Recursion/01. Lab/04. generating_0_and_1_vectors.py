"""
Generate all n-bit vectors of 0 and 1 in lexicographic order.

Example:
    input = 3
    output = 000
             001
             010
             011
             100
             101
             110
             111

"""
from typing import List


def generate(index: int, vector: List[int]) -> None:
    if index >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[index] = num
        generate(index + 1, vector)


n = int(input())

vec = [0] * n

generate(0, vec)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#3
