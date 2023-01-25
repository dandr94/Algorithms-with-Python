"""
A cable networking company plans to extend its existing cable network by connecting as many customers as possible within a fixed budget limit.
The company has calculated the cost of building some prospective connections.
You are given the existing cable network (a set of customers and connections between them),
along with the estimated connection costs between some pairs of customers and prospective customers.
A customer can only be connected to the network via a direct connection with an already connected customer.

"""
from queue import PriorityQueue
from typing import List, Set, Tuple



class Edge:
    def __init__(self, start: int, end: int, weight: int):
        self.start = start
        self.end = end
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def build_graph(nodes: int, edges: int) -> Tuple[List[List[int]], Set[int]]:
    graph = [[] for _ in range(nodes)]
    tree = set()

    for _ in range(edges):
        line = input().split()
        start, end, weight = [int(x) for x in line[:3]]

        edge = Edge(start, end, weight)

        graph[start].append(edge)
        graph[end].append(edge)

        if len(line) == 4:
            tree.add(start)
            tree.add(end)

    return graph, tree


def prim(graph: List[List[int]], tree: Set[int], budget_used: int) -> int:
    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1

        if min_edge.start in tree and min_edge.end not in tree:
            non_tree_node = min_edge.end
        elif min_edge.end in tree and min_edge.start not in tree:
            non_tree_node = min_edge.start

        if non_tree_node == -1:
            continue

        if budget_used + min_edge.weight > budget:
            break

        budget_used += min_edge.weight

        tree.add(non_tree_node)

        for edge in graph[non_tree_node]:
            pq.put(edge)

    return budget_used


budget = int(input())
nodes = int(input())
edges = int(input())

graph, tree = build_graph(nodes, edges)

pq = PriorityQueue()

for node in tree:
    for edge in graph[node]:
        pq.put(edge)

result = prim(graph, tree, 0)

print(f'Budget used: {result}')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3465#4
