"""
Find the MST of a given graph with Prim's algorithm.
"""
from typing import Dict, List, Set
from queue import PriorityQueue


class Edge:
    def __init__(self, first: int, second: int, weight: int):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def build_graph(edges: int) -> Dict[int, List[Edge]]:
    graph = {}

    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split(', ')]

        if first not in graph:
            graph[first] = []

        if second not in graph:
            graph[second] = []

        edge = Edge(first, second, weight)

        graph[first].append(edge)
        graph[second].append(edge)

    return graph


def prim(node: int, graph: Dict[int, List[Edge]], forest: Set[int], forest_edges: List[Edge]) -> None:
    forest.add(node)
    pq = PriorityQueue()

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest:
            non_tree_node = min_edge.first

        if non_tree_node == -1:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)

        for edge in graph[non_tree_node]:
            pq.put(edge)


edges = int(input())
graph = build_graph(edges)
forest = set()
forest_edges = []

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

for edge in forest_edges:
    print(f'{edge.first} - {edge.second}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3464#4
