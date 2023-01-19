"""
You will be given a graph from the console your task is to find the shortest path and print it back on the console.
The first line will be the number of Nodes - N the second one the number of Edges - E, then on each E line the edge in form {destination} – {source}.
On the last two lines, you will read the start node and the end node.
Print on the first line the length of the shortest path and the second the path itself.

"""
from collections import deque
from typing import List, Union, Deque


def bfs(node: int,
        graph: List[List[int]],
        visited: List[bool],
        parent: List[Union[None, int]],
        destination_node: int,
        queue: Deque[int]) -> None:

    if reached_end(node, destination_node):
        return

    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)
            parent[child] = node


def reached_end(node: int, destination: int) -> bool:
    if node == destination:
        return True

    return False


nodes = int(input())
edges = int(input())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()

    bfs(node, graph, visited, parent, destination_node, queue)

path = deque()
node = destination_node

while node:
    path.appendleft(node)
    node = parent[node]

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3464#0
