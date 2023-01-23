"""
We are given a directed graph. We are given also a set of pairs of vertices.
Find the shortest distance between each pair of vertices or -1 if there is no path connecting them.
On the first line, you will get N, the number of vertices in the graph.
On the second line, you will get P, the number of pairs between which to find the shortest distance.
On the next N lines will be the edges of the graph and on the next P lines, the pairs.

"""
from collections import deque
from typing import Dict, List, Union


def build_graph(nodes: int) -> Dict[int, List[int]]:
    graph = {}

    for _ in range(nodes):
        node, children_str = input().split(':')
        node = int(node)
        children = [int(x) for x in children_str.split(' ')] if children_str else []
        graph[node] = children

    return graph


def bfs(graph: Dict[int, List[int]], source: int, destination: int) -> Dict[int, Union[None, int]]:
    queue = deque([source])

    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()

        if node == destination:
            break

        for child in graph[node]:
            if child in visited:
                continue

            queue.append(child)
            visited.add(child)

            parent[child] = node

    return parent


def find_size(parent: Dict[int, Union[None, int]], destination: int) -> int:
    node = destination
    size = -1

    while node is not None:
        node = parent[node]
        size += 1

    return size


nodes = int(input())
pairs = int(input())

graph = build_graph(nodes)


for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = bfs(graph, source, destination)

    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_size(parent, destination)

    print(f'{{{source}, {destination}}} -> {size}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3465#0
