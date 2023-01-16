"""
Implement topological sorting over a directed graph of strings.
"""
from typing import Dict, Set, Deque, List, Any
from collections import deque


def dfs(node: str,
        graph: Dict[str, List[str]],
        visited: Set[str],
        cycles: Set,
        sorted_nodes: Deque[str]) -> None or Exception:

    if node in cycles:
        return Exception('Invalid topological sorting')

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


nodes = int(input())
graph = {}

for _ in range(nodes):
    line = input().split('->')
    node = line[0].strip()
    children = line[1].strip().split(', ') if line[1] else []
    graph[node] = children

visited = set()
cycles = set()
sorted_nodes = deque()

for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(f'Topological sorting:', *sorted_nodes, sep=', ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3462#1
