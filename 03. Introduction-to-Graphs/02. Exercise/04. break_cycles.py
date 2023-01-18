"""
You are given an undirected multi-graph.
Remove a minimal number of edges to make the graph acyclic (to break all cycles).
As a result, print the number of edges removed and the removed edges.
If several edges can be removed to break a certain cycle, remove the smallest of them in alphabetical order (smallest start vertex in alphabetical order and smallest end vertex in alphabetical order).
"""
from typing import Dict, List, Set


def dfs(node: str,
        destination: str,
        graph: Dict[str, List[str]],
        visited: Set[str]) -> None:

    if is_visited(node, visited):
        return

    visited.add(node)

    if is_equal(node, destination):
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def is_visited(node: str, visited: Set[str]) -> bool:
    if node in visited:
        return True

    return False

def is_equal(node: str, destination: str) -> bool:
    if node == destination: return True

    return False

def path_exists(source: str, destination: str, graph: Dict[str, List[str]]) -> bool:
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


nodes = int(input())

graph = {}
edges = []

for _ in range(nodes):
    line = input().split('->')
    node = line[0].strip()
    children = line[1].strip().split(' ') if line[1] else []
    graph[node] = children

    for child in children:
        edges.append((node, child))

result = []

edges = sorted(edges, key=lambda x: (x[0], x[1]))

for source, destination in edges:
    if source in graph[destination] or destination in graph[source]:
        graph[source].remove(destination)
        graph[destination].remove(source)

        if path_exists(source, destination, graph):
            result.append((source, destination))

        else:
            graph[source].append(destination)
            graph[destination].append(source)


print(f'Edges to remove: {len(result)}')

for source, destination in result:
    print(f'{source} - {destination}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3463#3
