"""
Given a not oriented graph as a form of edges, we need to find the number of connected components it has.

e.g.
graph = [[11,4],[4,12],[4,10],[12,10], [21,23],[1,2],[1,3]]

result = 3
"""

from collections import deque, defaultdict
from pprint import pprint


def build_graph(edges: list[list[int]]) -> tuple[dict[int, list[int]], set[int]]:
    graph: defaultdict[int, list[int]] = defaultdict(list)
    vertices = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        vertices.add(u)
        vertices.add(v)

    return graph, vertices


def bfs(start: int, graph: dict[int, list[int]], visited: set[int]) -> None:
    """
    We wil be doying the BFS here, and it will set the visited nodes, so basically
    every node visited will be added to the visited set, therefore if some nodes are not visited,
    it means that they are part of another component.
    """
    queue: deque[int] = deque([start])
    while queue:
        node: int = queue.popleft()

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


def count_connected_components(edges: list[list[int]]) -> int:
    # Stage 1: BUild the graph
    graph, vertices = build_graph(edges)

    # Stage 2: init the shared variables for the multiple loops
    visited: set[int] = set()
    components: int = 0

    for node in vertices:
        # If is not visited, it means that it is a new different component
        if node not in visited:
            bfs(node, graph, visited)
            components += 1

    pprint(graph)

    return components


if __name__ == "__main__":
    graph = [[11, 4], [4, 12], [4, 10], [12, 10], [21, 23], [1, 2], [1, 3]]
    print(f"Graph: {graph}")
    print(f"Number of connected components: {count_connected_components(graph)}")
