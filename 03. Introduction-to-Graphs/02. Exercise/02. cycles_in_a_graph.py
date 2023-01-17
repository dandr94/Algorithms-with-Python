"""
Write a program to check whether a directed graph is acyclic or holds any cycles.
The input ends with "End" line.
"""
from typing import Dict, List, Set


def dfs(node: str,
        graph: Dict[str, List[str]],
        visited: Set[str],
        cycles: Set[str]) -> None:

    if is_cycle(node, cycles):
        raise Exception

    if is_visited(node, visited):
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


def is_visited(node: str, visited: Set[str]) -> bool:
    if node in visited:
        return True

    return False


def is_cycle(node: str, cycles: Set[str]) -> bool:
    if node in cycles:
        return True

    return False


graph = {}

while True:
    line = input()

    if line == 'End':
        break

    node, destination = line.split('-')

    if node not in graph:
        graph[node] = []

    if destination not in graph:
        graph[destination] = []

    graph[node].append(destination)

visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3463#1
