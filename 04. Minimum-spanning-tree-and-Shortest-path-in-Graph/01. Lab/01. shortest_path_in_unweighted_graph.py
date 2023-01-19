"""
You will be given a graph from the console your task is to find the shortest path and print it back on the console.
The first line will be the number of Nodes - N the second one the number of Edges - E, then on each E line the edge in form {destination} – {source}.
On the last two lines, you will read the start node and the end node.
Print on the first line the length of the shortest path and the second the path itself.

"""
from collections import deque
from typing import List, Union, Deque


def build_graph(edges: int) -> List[List[int]]:
    graph = [[] for _ in range(nodes + 1)]

    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        graph[source].append(destination)

    return graph


def bfs(graph: List[List[int]],
        start_node: int,
        destination_node: int) -> List[Union[None, int]]:

    visited = [False] * len(graph)
    parent = [None for x in range(len(graph))]
    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if reached_end(node, destination_node):
            return parent

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                parent[child] = node


def reconstruct_path(parent: int, destination_node: int) -> Deque[int]:
    path = deque()
    node = destination_node

    while node:
        path.appendleft(node)
        node = parent[node]
    return path


def reached_end(node: int, destination: int) -> bool:
    if node == destination:
        return True

    return False


nodes = int(input())
edges = int(input())

graph = build_graph(edges)

start_node = int(input())
destination_node = int(input())

parent = bfs(graph, start_node, destination_node)
path = reconstruct_path(parent, destination_node)

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3464#0
