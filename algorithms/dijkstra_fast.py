from heapq import heappop, heappush


def dijkstra(
    graph: dict[str, list[tuple[str, int]]],
    start: str,
) -> dict[str, int]:

    heap: list[tuple[str, int]] = [(start, 0)]
    distances: dict[str, int] = {start: 0}

    while heap:
        curr_node, curr_distance = heappop(heap)

        if curr_distance > distances[curr_node]:
            continue

        for neighbour, weight in graph[curr_node]:
            new_distance = curr_distance + weight

            if new_distance < distances.get(neighbour, float("inf")):
                distances[neighbour] = new_distance
                heappush(heap, (neighbour, new_distance))

    return distances


if __name__ == "__main__":
    # The graph
    graph: dict[str, list[tuple[str, int]]] = {
        "A": [("B", 2), ("D", 8)],
        "B": [("A", 2), ("D", 5), ("E", 6)],
        "C": [("E", 9), ("F", 3)],
        "D": [("A", 8), ("B", 5), ("E", 3), ("F", 2)],
        "E": [("B", 6), ("C", 9), ("D", 3), ("F", 1)],
        "F": [("C", 3), ("D", 2), ("E", 1)],
    }

    # Find the shortest path value fropm A to C
    print(f"Distances with dijkstra: {dijkstra(graph, "A")}")
