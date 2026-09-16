def bellman_ford(
    vertices: int, edges: list[tuple[int, int, int]], start: int
) -> list[float]:
    """
    Finds the shortest distances from start to all vertices.

    edges:
        (from, to, weight)

    Returns -2 if there is a negative cycle reachable from start

    Finds the shortest path from a source vertex to every other vertex in a
    weighted graph. Unlike Dijkstra's algorithm, Bellman-Ford supports
    negative edge weights and can detect negative-weight cycles.

    Steps:
    1. Initialize the distance to the source vertex as 0 and the distance
    to every other vertex as infinity.

    2. Repeat the relaxation process V - 1 times, where V is the number
    of vertices in the graph.

    3. During each iteration, traverse every edge (u, v, weight):
    - If the source vertex u is reachable,
    - and distance[u] + weight < distance[v],
    - update distance[v] with the shorter value.

    4. Why V - 1 iterations?
    A shortest simple path can contain at most V - 1 edges. Therefore,
    after V - 1 complete relaxation rounds, all shortest paths must
    have been discovered if no negative cycle exists.

    5. Perform one additional pass over all edges.
    If any distance can still be improved, the graph contains a
    negative-weight cycle reachable from the source.

    Time Complexity:
        O(V * E)

    Space Complexity:
        O(V)

    Where:
        V = number of vertices
        E = number of edges
    """

    distances: list[float] = [float("inf")] * vertices
    distances[start] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):
        updated: bool = False

        for from_vertex, to_vertex, weight in edges:
            if distances[from_vertex] == float("inf"):
                continue

            if distances[from_vertex] + weight < distances[to_vertex]:
                distances[to_vertex] = distances[from_vertex] + weight
                updated = True

        # Optimization: If nothing changed, we are node
        if not updated:
            break

    # One extra pass to detect a negative cycle
    for from_vertex, to_vertex, weight in edges:
        if distances[from_vertex] == float("inf"):
            continue

        if distances[from_vertex] + weight < distances[to_vertex]:
            # Contains a negative cycle
            return [-2]

    return distances


if __name__ == "__main__":
    edges: list[tuple[int, int, int]] = [
        (0, 1, 4),
        (0, 2, 5),
        (2, 1, -3),
        (1, 3, 2),
    ]

    print(bellman_ford(4, edges, 0))
