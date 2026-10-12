def floyd_warshall_pairs_shortest_path(
    vertices: int, edges: list[tuple[int, int, int]]
) -> list[list[float]]:
    """
    Finds the shortest distances between every pair of vertices in a weighted graph.

    Floyd-Warshall works by progressively allowing each vertex to be used as an
    intermediate point in a path.

    a -> b   a -> b
             |    |
             c -> d

    Steps:
    1.  Create a VxV distance matrix initialized to infinity.
    2.  Set distance[i][i] = 0 for every vertex, since the distance
        from a vertex to itself is zero.
    3.  For every edge (start, end, weight), set:

            distance[start][end] = min(weight, distance[start][end])

        If multiple edges exist between the same pair of vertices, KEEP THE SMALLEST weight.

    4.  For every vertex k, consider it as an intermediate vertex between every pair (i,j).

            distance[i][j] = min(
                distance[i][j], distance[i][k] + distance[k][j]
            )

        "Is going from i -> k -> j shorter than the currently known path from i -> j?"

    5.  After processing all intermediate vertices, distance[i][j] contains the shortest distance from i to j.
    6.  If distance[i][j] < 0 for any vertex i, then the graph contains a negative-weight cycle.

    Time: O(V^3)  :O-<

    Space: O(V^2)

    Supports:
        - Directed graphs
        - Negative edge weights

    Does not produce valid shortest paths if a reachable negative cycle affects those paths.
    """

    distances: list[list[float]] = [[float("inf")] * vertices for _ in range(vertices)]

    # Init the distances for each node pointing to itself (diagonal)
    for vertex in range(vertices):
        distances[vertex][vertex] = 0

    # Set the distances from the edges, init the array basically
    for start, end, weight in edges:
        distances[start][end] = min(weight, distances[start][end])

    # Bruteforce all the combinations of start, middle and end vertices
    for middle in range(vertices):
        for start in range(vertices):
            for end in range(vertices):
                distances[start][end] = min(
                    distances[start][end],
                    distances[start][middle] + distances[middle][end],
                )

    return distances


if __name__ == "__main__":
    # Directed weighted graph:
    #
    #        4
    #   0 --------> 1
    #   |        / |
    # 8 |  -2 /    | 5
    #   v  v       v
    #   2 --------> 3
    #       2        |
    #                | 3
    #                v
    #                4
    #                |
    #                | 1
    #                └------> 1
    #
    # Edges:
    # 0 -> 1 (4)
    # 0 -> 2 (8)
    # 1 -> 2 (-2)
    # 1 -> 3 (5)
    # 2 -> 3 (2)
    # 3 -> 4 (3)
    # 4 -> 1 (1)
    edges: list[tuple[int, int, int]] = [
        (0, 1, 4),
        (0, 2, 8),
        (1, 2, -2),
        (1, 3, 5),
        (2, 3, 2),
        (3, 4, 3),
        (4, 1, 1),
    ]

    vertices: int = 5

    print(f"Distances: {floyd_warshall_pairs_shortest_path(vertices, edges)}")
    print(
        f"Distace from 0 to 4: {floyd_warshall_pairs_shortest_path(vertices, edges)[0][4]}"
    )
    print(
        f"Distace from 2 to 4: {floyd_warshall_pairs_shortest_path(vertices, edges)[2][4]}"
    )
