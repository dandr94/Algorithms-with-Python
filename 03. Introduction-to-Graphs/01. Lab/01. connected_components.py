"""
Implement the DFS algorithm (Depth-First-Search) to traverse a graph and find its connected components (nodes connected either directly, or through other nodes).
The graph nodes are numbered from 0 to n-1.
"""
from typing import List


def dfs(node: int, graph: List[List[int]], visited: List[bool], component: List[int]) -> None:
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [int(x) for x in line.split()] if line else []
    graph.append(children)

visited = [False] * nodes

for node in range(nodes):
    component = []
    dfs(node, graph, visited, component)
    if component:
        print(f'Connected component: {" ".join(str(x) for x in component)}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3462#0
