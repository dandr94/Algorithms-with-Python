"""
Write a program that simulates the execution of n nested loops from 1 to n which prints the values of all its iteration variables at any given time on a single line.
Use recursion.
"""
from typing import List


def generate(index: int, vector: List[int]) -> None:
    if index >= len(vector):
        print(*vector, sep=' ')
        return

    for num in range(1, n + 1):
        vector[index] = num
        generate(index + 1, vector)


n = int(input())

vec = [0] * n

generate(0, vec)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3460#1
