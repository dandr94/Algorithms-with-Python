from typing import Dict, List, Set


def dfs(n: int, g: Dict[int, List[int]], v: Set[int]) -> None:
    if n in v:
        return

    v.add(n)

    for c in g[n]:
        dfs(c, g, v)

    print(n, end=' ')


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: []
}

visited = set()

for node in graph:
    dfs(node, graph, visited)
