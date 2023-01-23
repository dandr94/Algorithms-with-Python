"""
Find the MST of a given graph with Kruskal's algorithm.
"""
from typing import List


class Edge:
    def __init__(self, first: int, second: int, weight: int):
        self.first = first
        self.second = second
        self.weight = weight


def build_graph(edges: int) -> List[Edge]:
    graph = []

    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split(', ')]

        graph.append(Edge(first, second, weight))

    return graph


def find_max_node(graph: List[Edge]) -> int:
    max_node = float('-inf')

    for node in graph:
        max_value = max(node.first, node.second, max_node)

        if max_node < max_value:
            max_node = max_value

    return max_node


def find_root(parent: List[int], node: int) -> int:
    while node != parent[node]:
        node = parent[node]

    return node


def kruskal(graph: List[Edge], parent: List[int]) -> List[Edge]:
    forest = []

    for edge in graph:
        first_node_root = find_root(parent, edge.first)
        second_node_root = find_root(parent, edge.second)

        if first_node_root != second_node_root:
            parent[first_node_root] = second_node_root
            forest.append(edge)

    return forest


def print_results(forest: List[Edge]) -> None:
    for edge in forest:
        print(f'{edge.first} - {edge.second}')


edges = int(input())

graph = sorted(build_graph(edges), key=lambda e: e.weight)

max_node = find_max_node(graph)

parent = [n for n in range(max_node + 1)]

forest = kruskal(graph, parent)

print_results(forest)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3464#3
