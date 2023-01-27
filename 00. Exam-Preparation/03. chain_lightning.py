"""
When lightning falls, it damages all connected neighborhoods, but the damage halves with each jump (integer division).
The lightning always jumps to a neighborhood that has the smallest distance to any neighborhood already damaged.
Note that lightning doesn’t necessarily fork only at its tail.
Also, the same lightning cannot damage the same neighborhood twice.
Your job is to find the condition of the most heavily damaged neighborhood after multiple strikes on top of different city neighborhoods,
so a team of highly skilled technicians can be dispatched.
"""
from queue import PriorityQueue
from typing import List, Dict


class Edge:
    def __init__(self, first: int, second: int, weight: int):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def build_graph(n: int, d: int) -> Dict[int, List[Edge]]:
    graph = {node: [] for node in range(n)}

    for _ in range(d):
        first, second, weight = [int(x) for x in input().split()]

        edge = Edge(first, second, weight)

        graph[first].append(edge)
        graph[second].append(edge)

    return graph


def calc_damage(jumps: int, damage: int) -> int:
    for _ in range(jumps):
        damage //= 2

    return damage


def prim(node: int, damage: int, damage_by_node: List[int], graph: Dict[int, List[Edge]]) -> None:
    damage_by_node[node] += damage

    tree = {node}

    jumps = [0] * len(graph)

    pq = PriorityQueue()

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = -1, -1

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        elif min_edge.second in tree and min_edge.first not in tree:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        tree.add(non_tree_node)

        for edge in graph[non_tree_node]:
            pq.put(edge)

        jumps[non_tree_node] = jumps[tree_node] + 1

        damage_by_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


neighborhoods = int(input())
distance = int(input())
lightning = int(input())

graph = build_graph(neighborhoods, distance)

damage_by_node = [0] * neighborhoods

for _ in range(lightning):
    node, damage = [int(x) for x in input().split()]

    prim(node, damage, damage_by_node, graph)

print(max(damage_by_node))

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3474#2
