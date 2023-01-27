"""
The greatest storyteller of all time needs your help.
He has his stories, however, they got all mixed up his storytelling needs to be in the correct order and you need to fix that order.
You will be given the stories in the following format on a single line until the command "End" is received.
{preStory} -> {postStory1} {postStory2} {postStoryn-1}
You have to read the stories data and then print the stories in the correct order according to the description above.
Keep in mind that the structure above represents relation in which any story can be preStory or postStory in different input lines.
"""
from collections import deque
from typing import Dict, List, Set, Deque


def build_graph() -> Dict[str, List[str]]:
    graph = {}

    while True:

        line = input()

        if line == 'End':
            break

        node, children = [x.strip() for x in line.split('->')]

        graph[node] = children.split()

    return graph


def dfs(node: str, graph: Dict[str, List[str]], visited: Set[str], component: Deque[str]) -> None:
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.appendleft(node)


graph = build_graph()
visited = set()
component = deque()

for node in graph:
    dfs(node, graph, visited, component)

print(*component, sep=' ')

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3474#0
