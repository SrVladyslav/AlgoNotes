"""
We are provided with an oriented graph as a list of edges, where each edge is a pair [u, v]
and represents the edge from vertex u to vertex v. We are also provided with a starting point start and
last point finish. We need to find the shortest path from start to finish. If the path does not exist,
then return -1.

e.g.
edges = [[0,1], [0,2], [1,3], [2,3],[3,4]]
start = 0
finish = 4

response = 2
"""

from collections import deque
from pprint import pprint
from patterns.graphs.lib import graph_from_edges


def find_shortest_path(graph: dict[int, list[int]], start: int, finish: int) -> int:
    # We will be using BFS here too, also with the counter for the distance
    queue: deque[tuple[int, int]] = deque(
        [(start, 0)]
    )  # Start represents the current node where we are starting
    visited: set[int] = {
        start
    }  # Visited nodes, so basically we are doing the typical BFS

    # Directions are not needed since we are using a normal graph and not some special representation

    while queue:
        # get the first element from the list and process it
        node, distance = queue.popleft()

        # Check if we are at the end or not
        if node == finish:
            return distance

        # If we are not at the end, we should check all the neighbours to the current node possible
        for neighbour in graph.get(node, []):
            # Check if they are visited or not
            if neighbour not in visited:
                queue.append((neighbour, distance + 1))

    return -1


if __name__ == "__main__":
    edges: list[list[int]] = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
    start: int = 0
    finish: int = 4

    graph: dict[int, list[int]] = graph_from_edges(edges, is_directed=True)
    pprint(graph)
    print(
        f"Shortest path from {start} to {finish}: {find_shortest_path(graph, start, finish)}"
    )
