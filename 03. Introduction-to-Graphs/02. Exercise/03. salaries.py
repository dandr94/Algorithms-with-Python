"""
We have a hierarchy between the employees in a company.
Employees can have one or several direct managers.
People who manage nobody are called regular employees and their salaries are 1.
People who manage at least one employee are called managers.
Each manager takes a salary which is equal to the sum of the salaries of their directly managed employees.
If we have N employees, they will be indexed from 0 to N – 1.
For each employee, you will be given a string with N symbols.
The symbols are either 'Y' or 'N', showing all employees that are managed by the current employee

"""
from typing import List, Union


def dfs(node: int, graph: List[List[int]], memo: List[Union[None, int]]) -> int:
    if is_already_calc(node, memo):
        return memo[node]

    if is_regular(node, graph):
        memo[node] = 1
        return 1

    salary = 0

    for child in graph[node]:
        salary += dfs(child, graph, memo)

    memo[node] = salary

    return salary


def is_regular(node: int, graph: List[List[int]]) -> bool:
    if len(graph[node]) == 0:
        return True

    return False


def is_already_calc(node: int, memo: List[int]) -> bool:
    if memo[node]:
        return True

    return False


n = int(input())
graph = []

for _ in range(n):
    line = input()
    children = []

    for index, state in enumerate(line):
        if state == 'Y':
            children.append(index)

    graph.append(children)

memo = [None] * n
result = 0

for node in range(n):
    salary = dfs(node, graph, memo)
    result += salary

print(result)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3463#2
