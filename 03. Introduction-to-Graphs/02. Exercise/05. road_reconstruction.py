"""
Write a program that finds all the roads without which buildings in the city will become unreachable.
You will receive how many buildings the town has on the first line, then you will receive the number of streets and finally,
for each street, you will receive which buildings it connects.
Find all the streets that are important and cannot be removed and print them in ascending order (e. g. 3 0 should be printed as 0 3).

"""
from typing import List


def dfs(node: int, graph: List[List[int]], visited: List[bool]) -> None:
    if is_visited(node, visited):
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


def is_visited(node: int, visited: List[bool]) -> bool:
    if visited[node]:
        return True

    return False

n_nodes = int(input())
n_edges = int(input())

graph = [[] for _ in range(n_nodes)]
edges = []

for _ in range(n_edges):
    source, destination = [int(x) for x in input().split(' - ')]
    graph[source].append(destination)
    graph[destination].append(source)
    edges.append((min(source, destination), max(source, destination)))

print('Important streets:')

for source, destination in edges:
    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = [False] * n_nodes

    dfs(source, graph, visited)

    if not all(visited):
        print(f'{source} {destination}')

    graph[source].append(destination)
    graph[destination].append(source)


# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3463#4