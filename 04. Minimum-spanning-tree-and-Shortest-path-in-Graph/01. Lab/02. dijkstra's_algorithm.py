"""
Try to implement the optimized version of Dijkstra’s algorithm using a priority queue.
"""
from collections import deque
from queue import PriorityQueue
from typing import Dict, List, Union, Deque


class Edge:
    def __init__(self, source: int, destination: int, weight: int):
        self.source = source
        self.destination = destination
        self.weight = weight


def build_graph(edges: int) -> Dict[int, List[Edge]]:
    graph = {}

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(', ')]

        if source not in graph:
            graph[source] = []

        if destination not in graph:
            graph[destination] = []

        graph[source].append(Edge(source, destination, weight))

    return graph


def bfs(graph: Dict[int, List[Edge]], start: int, end: int):
    max_node = max(graph.keys())
    distance = [float('inf')] * (max_node + 1)
    parent = [None] * (max_node + 1)

    distance[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        min_distance, node = pq.get()

        if node == end:
            return parent, distance

        for edge in graph[node]:
            new_distance = min_distance + edge.weight

            if new_distance < distance[edge.destination]:
                distance[edge.destination] = new_distance
                parent[edge.destination] = node
                pq.put((new_distance, edge.destination))

    return parent, distance


def reconstruct_path(parent: List[Union[None, int]], end: int) -> Deque[int]:
    path = deque()

    node = end

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


def print_results(distance: List[Union[int, float]], parent: List[Union[None, int]], end: int) -> None:
    if distance[end] == float('inf'):
        print('There is no such path.')
    else:
        print(distance[end])

        path = reconstruct_path(parent, end)

        print(*path, sep=' ')


edges = int(input())

graph = build_graph(edges)

start = int(input())
end = int(input())

parent, distance = bfs(graph, start, end)

print_results(distance, parent, end)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3464#1
