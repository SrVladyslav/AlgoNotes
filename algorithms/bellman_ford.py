def bellman_ford(
    vertices: int, edges: list[tuple[int, int, int]], start: int
) -> list[float]:
    """
    Finds the shortest distances from start to all vertices.

    edges:
        (from, to, weight)

    Returns -2 if there is a negative cycle reachable from start

    Time: O(V*E)
    Memory: O(V)
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
