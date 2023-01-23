"""
Find the shortest path in a graph and print it as a sequence from S vertex to D vertex.
Implement the Bellman-Ford algorithm.

"""
from collections import deque
from typing import List, Deque, Union


class Edge:
    def __init__(self, source: int, destination: int, weight: int):
        self.source = source
        self.destination = destination
        self.weight = weight


def build_graph(edges: int) -> List[Edge]:
    graph = []

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split()]

        graph.append(Edge(source, destination, weight))

    return graph


def bfs(graph: List[Edge], start: int, end: int) -> None:
    distance = [float('inf')] * (nodes + 1)
    distance[start] = 0
    parent = [None] * (nodes + 1)

    for _ in range(nodes - 1):
        updated = False
        for edge in graph:
            if distance[edge.source] == float('inf'):
                continue
            new_distance = distance[edge.source] + edge.weight

            if new_distance < distance[edge.destination]:
                distance[edge.destination] = new_distance
                parent[edge.destination] = edge.source
                updated = True

        if not updated:
            break

    return print_results(graph, parent, distance, end)


def is_cycle(graph: List[Edge], distance: List[Union[float, int]]) -> bool:
    for edge in graph:
        new_distance = distance[edge.source] + edge.weight

        if new_distance < distance[edge.destination]:
            return True

    return False


def reconstruct_path(parent: List[Union[None, int]], end: int) -> Deque[int]:
    path = deque()
    node = end

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


def print_results(graph: List[Edge],
                  parent: List[Union[None, int]],
                  distance: List[Union[float, int]],
                  end: int) -> None:

    if is_cycle(graph, distance):
        print('Negative Cycle Detected')
    else:
        path = reconstruct_path(parent, end)

        print(*path, sep=' ')
        print(distance[end])


nodes = int(input())
edges = int(input())

graph = build_graph(edges)

start = int(input())
end = int(input())

bfs(graph, start, end)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3464#2
