"""
You now live in a new country, and you want to start a tour and visit every town in the country and since you are new in the country your finances are minimized, so you want your trip to be as cheap as possible.
You will be given the amount of the cities on the first line, then the amount of the roads (n), and on the next n lines you will receive which tows the road connects and the cost to use it.
Assume you can start from any town and your target is to visit every one of them with the minimum cost.

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
        first, second, weight = [int(x) for x in input().split(' - ')]

        edge = Edge(first, second, weight)

        graph.append(edge)

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
    total_cost = sum([x.weight for x in forest])

    print(f'Total cost: {total_cost}')


nodes = int(input())
edges = int(input())

graph = sorted(build_graph(edges), key=lambda e: e.weight)

parent = [n for n in range(nodes)]

forest = kruskal(graph, parent)

print_results(forest)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3465#2
