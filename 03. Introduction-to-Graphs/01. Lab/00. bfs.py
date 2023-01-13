from collections import deque
from typing import Dict, List, Set


def bfs(n: int, g: Dict[int, List[int]], v: Set[int]) -> None:
    if n in v:
        return

    queue = deque([n])

    v.add(n)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for c in g[current_node]:
            if c not in v:
                v.add(c)
                queue.append(c)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: []
}

visited = set()

for node in graph:
    bfs(node, graph, visited)
