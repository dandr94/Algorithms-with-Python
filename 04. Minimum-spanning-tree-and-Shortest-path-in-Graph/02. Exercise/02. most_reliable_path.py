"""
We have a set of towns and some of them are connected by direct paths.
Each path has a coefficient of reliability (in percentage): the chance to pass without incidents.
Your goal is to compute the most reliable path between two given nodes.
Assume all percentages will be integer numbers and round the result to the second digit after the decimal separator.
"""
from collections import deque
from queue import PriorityQueue
from typing import List, Union, Deque


class Edge:
    def __init__(self, first: int, second: int, weight: int):
        self.first = first
        self.second = second
        self.weight = weight


def build_graph(nodes: int, edges: int) -> List[List[Edge]]:
    graph = [[] for _ in range(nodes)]

    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split()]

        edge = Edge(first, second, weight)

        graph[first].append(edge)
        graph[second].append(edge)

    return graph


def bfs(nodes: int, graph: List[List[Edge]], start: int, end: int) -> None:
    distance = [float('-inf')] * nodes
    parent = [None] * nodes

    distance[start] = 100

    pq = PriorityQueue()
    pq.put((-100, start))

    while not pq.empty():
        max_distance, node = pq.get()

        if node == end:
            return print_results(distance, parent, end)

        for edge in graph[node]:
            child = edge.second if edge.first == node else edge.first
            new_distance = -max_distance * edge.weight / 100

            if new_distance > distance[child]:
                distance[child] = new_distance
                parent[child] = node
                pq.put((-new_distance, child))

    return print_results(distance, parent, end)


def reconstruct_path(parent: List[Union[None, int]], end: int) -> Deque[int]:
    path = deque()

    node = end

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


def print_results(distance: List[Union[int, float]], parent: List[Union[None, int]], end: int) -> None:
    print(f'Most reliable path reliability: {distance[end]:.2f}%')

    path = reconstruct_path(parent, end)

    print(*path, sep=' -> ')


nodes = int(input())
edges = int(input())
graph = build_graph(nodes, edges)
start = int(input())
end = int(input())
bfs(nodes, graph, start, end)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3465#1
